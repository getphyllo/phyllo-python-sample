from fastapi import HTTPException
import requests
from requests.auth import HTTPBasicAuth

from app.utils.phyllo_api.phyllo_credential import CLIENT_ID, CLIENT_SECRET, BASE_URL


def get_all(query_param: dict):
    try:
        response = requests.get(BASE_URL + "/v1/accounts", auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
                                params=query_param)
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def get_by_id(id: str):
    try:
        response = requests.get(BASE_URL + f"/v1/accounts/{id}", auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")
