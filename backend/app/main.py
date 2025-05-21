from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import (
    admin_only_router,
    get_me_router,
    login_router,
    register_router,
)

app = FastAPI(title="AQsis Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(login_router, prefix="/api/v1", tags=["Login"])
app.include_router(register_router, prefix="/api/v1", tags=["Register"])
app.include_router(get_me_router, prefix="/api/v1", tags=["Get Me"])
app.include_router(admin_only_router, prefix="/api/v1", tags=["Admin Only"])

