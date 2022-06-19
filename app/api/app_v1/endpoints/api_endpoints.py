from fastapi import APIRouter

from app.api.app_v1.endpoints import api_user, api_sdk_token, api_work_platform, api_account, api_profile, api_social, \
    api_income, api_audience

api_router = APIRouter()
api_router.include_router(api_user.api_router, prefix="/users")
api_router.include_router(api_work_platform.api_router, prefix="/work-platforms")
api_router.include_router(api_sdk_token.api_router, prefix="/sdk-tokens")
api_router.include_router(api_account.api_router, prefix="/accounts")
api_router.include_router(api_profile.api_router, prefix="/profiles")
api_router.include_router(api_social.api_router, prefix="/social")
api_router.include_router(api_income.api_router, prefix="/income")
api_router.include_router(api_audience.api_router, prefix="/audience")
