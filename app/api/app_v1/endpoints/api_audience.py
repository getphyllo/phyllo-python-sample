from typing import Optional

from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("")
async def get_audience(account_id: Optional[str] = None):
    query_param = {"account_id": account_id}
    return a.get_all(query_param=query_param)
