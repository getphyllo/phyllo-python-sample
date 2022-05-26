from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter
from pydantic import conint

from app.utils.phyllo_api import profile

api_router = APIRouter()


@api_router.get("")
async def get_profiles(user_id: Optional[str] = None, account_id: Optional[str] = None,
                       work_platform_id: Optional[str] = None, limit: Optional[conint(ge=1, le=100)] = 10,
                       offset: Optional[int] = 0):
    query_param = {"limit": limit, "offset": offset, "work_platform_id": work_platform_id,
                   "user_id": user_id, "account_id": account_id}
    return profile.get_all(query_param=query_param)


@api_router.get("/{id}", status_code=HTTPStatus.OK)
async def get_profile_by_id(id: str):
    return profile.get_by_id(id=id)
