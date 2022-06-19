from datetime import date
from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter
from pydantic import conint

from app.services import content

api_router = APIRouter()


@api_router.get("/contents", status_code=HTTPStatus.OK)
async def get_contents(user_id: Optional[str] = None, account_id: Optional[str] = None,
                       work_platform_id: Optional[str] = None,
                       limit: Optional[conint(ge=1, le=100)] = 10, offset: Optional[int] = 0,
                       from_date: Optional[date] = None,
                       to_date: Optional[date] = None):
    query_param = {"limit": limit, "offset": offset, "user_id": user_id, "work_platform_id": work_platform_id,
                   "account_id": account_id, "from_date": from_date, "to_date": to_date}

    return content.get_all(query_param=query_param)


@api_router.get("/contents/{id}")
async def get_content_by_id(id: str):
    return content.get_by_id(id=id)
