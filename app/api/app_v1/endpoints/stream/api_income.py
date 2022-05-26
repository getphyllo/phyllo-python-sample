from datetime import date
from typing import Optional

from fastapi import APIRouter
from pydantic import conint

from app.utils.phyllo_api import income

api_router = APIRouter()


@api_router.get("/accounts")
async def get_accounts_income(income_from_date: Optional[date] = None,
                              income_to_date: Optional[date] = None,
                              limit: Optional[conint(ge=1, le=100)] = 10,
                              offset: Optional[int] = 0):
    query_param = {"income_from_date": income_from_date, "income_to_date": income_to_date,
                   "limit": limit, "offset": offset}
    return income.get_all(query_param=query_param)


@api_router.get("/accounts/{id}")
async def get_accounts_income_by_id(id: str,
                                    income_from_date: Optional[date] = None,
                                    income_to_date: Optional[date] = None):
    query_param = {"income_from_date": income_from_date, "income_to_date": income_to_date}
    return income.get_by_id(id=id, query_param=query_param)
