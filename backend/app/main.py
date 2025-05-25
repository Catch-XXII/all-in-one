from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import (
    admin_only_router,
    deactivate_user_router,
    get_me_router,
    login_router,
    register_router,
)
from app.core.config import settings

app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    contact={
        "name": "Cuneyd Kaya",
        "email": "cgultekink@gmail.com",
        "url": "https://qasis.ai",
    },
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
        "docExpansion": "list",
        "displayRequestDuration": True,
    },
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc
    debug=True,
)

allow_origin_regex = (
    r"http://192\.168\.1\.\d+:5173"  # covers all 192.168.1.X:5173 origins
    if settings.ENVIRONMENT == "development"
    else None
)

allow_origins = (
    [settings.FRONTEND_ORIGIN] if settings.ENVIRONMENT != "development" else []
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_origin_regex=allow_origin_regex,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(login_router, prefix="/api/v1", tags=["Login"])
app.include_router(register_router, prefix="/api/v1", tags=["Register"])
app.include_router(get_me_router, prefix="/api/v1", tags=["Who Am I"])
app.include_router(admin_only_router, prefix="/api/v1", tags=["Admin Only"])
app.include_router(deactivate_user_router, prefix="/api/v1", tags=["Admin Only"])
