from .admin_only import router as admin_only_router
from .analyze import router as analyze_router
from .deactivate_user import router as deactivate_user_router
from .login import router as login_router
from .register import router as register_router
from .who_am_i import router as get_me_router

__all__ = [
    "login_router",
    "register_router",
    "get_me_router",
    "admin_only_router",
    "deactivate_user_router",
    "analyze_router",
]
