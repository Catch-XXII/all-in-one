from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.deps.auth_deps import require_admin
from app.db.models.user import User

router = APIRouter()


@router.get("/admin-only", summary="Protected admin-only test endpoint")
async def read_admin_data(admin: Annotated[User, Depends(require_admin)]):
    return {"message": f"Hello Admin {admin.email}!"}
