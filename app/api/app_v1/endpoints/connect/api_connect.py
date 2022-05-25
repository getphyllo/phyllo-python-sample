from fastapi import APIRouter

from app.api.app_v1.endpoints.connect import api_user

api_router = APIRouter(tags=["CONNECT"])
api_router.include_router(api_user.api_router, prefix="/users")
