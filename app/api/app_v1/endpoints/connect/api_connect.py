from fastapi import APIRouter

from app.api.app_v1.endpoints.connect import api_user, api_work_platform, api_sdk_token

api_router = APIRouter(tags=["CONNECT"])
api_router.include_router(api_user.api_router, prefix="/users")
api_router.include_router(api_work_platform.api_router, prefix="/work-platforms")
api_router.include_router(api_sdk_token.api_router, prefix="/sdk-tokens")
