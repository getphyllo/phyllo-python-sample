from fastapi import APIRouter
from starlette.requests import Request

from app.schemas.sdk_token import SdkTokenRequest
from app.utils.phyllo_api import sdk_token

api_router = APIRouter()


@api_router.post("")
def create_token(token_request: SdkTokenRequest, request: Request):
    body = token_request.__dict__
    return sdk_token.create(body=body)
