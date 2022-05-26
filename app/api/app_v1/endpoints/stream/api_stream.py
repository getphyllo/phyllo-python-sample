from fastapi import APIRouter

from app.api.app_v1.endpoints.stream import api_profile, api_income, api_account, api_social

api_router = APIRouter(tags=["STREAM"])
api_router.include_router(api_account.api_router, prefix="/accounts")
api_router.include_router(api_profile.api_router, prefix="/profiles")
api_router.include_router(api_social.api_router, prefix="/social")
api_router.include_router(api_income.api_router, prefix="/income")
