from app.api.v1.endpoints import health, hello, auth
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AQsis Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/v1", tags=["Health"])
app.include_router(hello.router, prefix="/v1", tags=["Hello"])
app.include_router(auth.router, prefix="/v1", tags=["Auth"])
