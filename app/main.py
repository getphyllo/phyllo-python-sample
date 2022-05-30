from http import HTTPStatus
from http.client import INTERNAL_SERVER_ERROR, BAD_REQUEST

import uvicorn
from fastapi import FastAPI
from sqlalchemy.exc import DataError
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.api.app_v1.endpoints import api_endpoints

app = FastAPI()

app.include_router(api_endpoints.api_router, prefix='/v1')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
def custom_http_exception_handler(request, exc):
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    message = INTERNAL_SERVER_ERROR
    if type(exc) is DataError:
        status_code = HTTPStatus.BAD_REQUEST
        message = BAD_REQUEST
    return JSONResponse(
        status_code=status_code,
        content={"message": message},
    )


@app.get("/")
def root():
    return {"message": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8870, proxy_headers=True, forwarded_allow_ips="*",
                use_colors=True)
