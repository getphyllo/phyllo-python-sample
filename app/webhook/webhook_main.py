import uvicorn
from fastapi import FastAPI
from starlette.requests import Request

from app.webhook.webhook_service import analyse_and_store_webhook
from app.webhook.webhook_setup import configure_webhook

app = FastAPI()


@app.post("/")
async def receive_webhook(request: Request):
    return await analyse_and_store_webhook(request=request)


@app.on_event("startup")
async def startup_event():
    configure_webhook()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9003, forwarded_allow_ips="*", )
