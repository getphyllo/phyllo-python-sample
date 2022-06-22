import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


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


@app.get("/")
def root():
    return {"message": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000, forwarded_allow_ips="*")
