from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import (
    admin_only_router,
    analyze_router,
    deactivate_user_router,
    get_me_router,
    login_router,
    register_router,
)
from app.core.config import settings
from app.core.rate_limiter import (
    default_rate_limit,
    login_rate_limit,
    setup_rate_limiter,
    strict_rate_limit,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await setup_rate_limiter()
    yield
    # Shut down
    # Add cleanup code here if needed


app = FastAPI(
    lifespan=lifespan,
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

if settings.ENVIRONMENT == "production":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.FRONTEND_ORIGIN],
        allow_origin_regex=None,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Only what you need
        allow_headers=["Authorization", "Content-Type"],  # Only what you need
    )
else:
    # Development configuration
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[],
        allow_origin_regex=r"http://192\.168\.1\.\d+:5173",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(
    login_router,
    prefix="/api/v1",
    tags=["Login"],
    dependencies=[Depends(login_rate_limit())],
)
app.include_router(
    register_router,
    prefix="/api/v1",
    tags=["Register"],
    dependencies=[Depends(strict_rate_limit())],
)
app.include_router(
    get_me_router,
    prefix="/api/v1",
    tags=["Who Am I"],
    dependencies=[Depends(default_rate_limit())],
)
app.include_router(
    admin_only_router,
    prefix="/api/v1",
    tags=["Admin Only"],
    dependencies=[Depends(default_rate_limit())],
)
app.include_router(
    deactivate_user_router,
    prefix="/api/v1",
    tags=["Admin Only"],
    dependencies=[Depends(default_rate_limit())],
)
app.include_router(
    analyze_router,
    prefix="/api/v1",
    tags=["Analyze"],
    dependencies=[Depends(default_rate_limit())],
)
