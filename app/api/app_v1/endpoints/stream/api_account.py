from typing import Optional

from fastapi import APIRouter
from pydantic import conint

from app.utils.phyllo_api import account

api_router = APIRouter()


@api_router.get("")
async def get_accounts(limit: Optional[conint(ge=1, le=100)] = 10,
                       offset: Optional[int] = 0,
                       user_id: Optional[str] = None, work_platform_id: Optional[str] = None):
    query_param = {"limit": limit, "offset": offset, "user_id": user_id, "work_platform_id": work_platform_id}
    return account.get_all(query_param=query_param)


@api_router.get("/{id}")
async def get_account_by_id(id: str):
    return account.get_by_id(id=id)
