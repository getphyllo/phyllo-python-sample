from typing import Optional

from fastapi import APIRouter
from pydantic import conint
from starlette.requests import Request

from app.schemas.user import UserRequest
from app.utils.phyllo_api import user

api_router = APIRouter()


@api_router.post("")
def create_user(user_request: UserRequest, request: Request):
    body = user_request.dict()
    return user.create(body=body)


@api_router.get("")
def get_users(limit: Optional[conint(ge=1, le=100)] = 10,
              offset: Optional[int] = 0, ):
    query_params = {"limit": limit, "offset": offset}
    return user.get_all(query_param=query_params)


@api_router.get("/{id}")
def get_user_by_id(id: str):
    return user.get_by_id(id=id)
