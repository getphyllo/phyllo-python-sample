from fastapi import HTTPException
import requests
from requests.auth import HTTPBasicAuth

from app.utils.phyllo_api.phyllo_credential import CLIENT_ID, CLIENT_SECRET, BASE_URL


def create(body: dict):
    try:
        response = requests.post(BASE_URL + "/v1/sdk-tokens", json=body,
                                 auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")
