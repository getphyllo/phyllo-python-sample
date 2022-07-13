import requests
from fastapi import HTTPException
from requests.auth import HTTPBasicAuth

from app.utils.phyllo_config import CLIENT_ID, CLIENT_SECRET, BASE_URL, WEBHOOK_URL, SUPPORTED_WEBHOOK_EVENTS


def get_all_account(query_param: dict):
    try:
        response = requests.get(BASE_URL + "/v1/accounts", auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
                                params=query_param)
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def get_account_by_id(id: str):
    try:
        response = requests.get(BASE_URL + f"/v1/accounts/{id}", auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def get_all_content(query_param: dict):
    try:
        response = requests.get(BASE_URL + "/v1/social/contents",
                                auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
                                params=query_param)
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def get_content_by_id(id: str):
    try:
        response = requests.get(BASE_URL + f"/v1/social/contents/{id}",
                                auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def get_all_income(query_param: dict):
    try:
        response = requests.get(BASE_URL + "/v1/income/accounts", auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
                                params=query_param)
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def get_income_by_id(id: str, query_param: dict):
    try:
        response = requests.get(BASE_URL + f"/v1/income/accounts/{id}", params=query_param,
                                auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def get_all_profile(query_param: dict):
    try:
        response = requests.get(BASE_URL + "/v1/profiles", auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
                                params=query_param)
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def get_profile_by_id(id: str):
    try:
        response = requests.get(BASE_URL + f"/v1/profiles/{id}", auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def create_sdk_token(body: dict):
    try:
        response = requests.post(BASE_URL + "/v1/sdk-tokens", json=body,
                                 auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def create_user(body: dict):
    try:
        response = requests.post(BASE_URL + "/v1/users", json=body,
                                 auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def get_all_user(query_param: dict):
    try:
        response = requests.get(BASE_URL + "/v1/users", auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
                                params=query_param)
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def get_user_by_id(id: str):
    try:
        response = requests.get(BASE_URL + f"/v1/users/{id}", auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def get_all_work_platfrom(query_param: dict):
    try:
        response = requests.get(BASE_URL + "/v1/work-platforms", auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
                                params=query_param)
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def get_work_platform_by_id(id: str):
    try:
        response = requests.get(BASE_URL + f"/v1/work-platforms/{id}", auth=HTTPBasicAuth(CLIENT_ID,
                                                                                          CLIENT_SECRET))
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def get_audience(query_param: dict):
    try:
        response = requests.get(BASE_URL + "/v1/audience", auth=HTTPBasicAuth(CLIENT_ID,
                                                                              CLIENT_SECRET), params=query_param)
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def create_webhook():
    try:
        request_body = {
            "url": WEBHOOK_URL,
            "events": SUPPORTED_WEBHOOK_EVENTS,
        }
        response = requests.post(BASE_URL + "/v1/webhooks", auth=HTTPBasicAuth(CLIENT_ID,
                                                                               CLIENT_SECRET), json=request_body)
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def get_all_webhooks():
    try:
        response = requests.get(BASE_URL + "/v1/webhooks", auth=HTTPBasicAuth(CLIENT_ID,
                                                                              CLIENT_SECRET))
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def update_webhook(id: str):
    try:
        request_body = {
            "url": WEBHOOK_URL,
            "events": SUPPORTED_WEBHOOK_EVENTS
        }
        response = requests.put(BASE_URL + f"/v1/webhooks/{id}", auth=HTTPBasicAuth(CLIENT_ID,
                                                                                     CLIENT_SECRET), json=request_body)
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")
