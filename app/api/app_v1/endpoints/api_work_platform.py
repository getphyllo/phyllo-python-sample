from typing import Optional

from fastapi import APIRouter
from pydantic import conint

from app.services import work_platform

api_router = APIRouter()


@api_router.get("/{id}")
def get_work_platform_by_id(id: str):
    return work_platform.get_by_id(id=id)


@api_router.get("")
def get_work_platforms(name: Optional[str] = None, limit: Optional[conint(ge=1, le=100)] = 10,
                       offset: Optional[int] = 0):
    query_params = {"limit": limit, "offset": offset, "name": name}
    return work_platform.get_all(query_param=query_params)
