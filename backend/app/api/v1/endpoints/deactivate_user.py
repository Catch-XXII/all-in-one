from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps.auth_deps import get_current_user
from app.db.database import get_db
from app.db.models import User

router = APIRouter()


class UserDeleteRequest(BaseModel):
    email: EmailStr


@router.post(
    "/admin/deactivate-user",
    summary="Deactivate a user by email (admin only)",
)
async def deactivate_user(
    data: UserDeleteRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Forbidden You are not superuser")

    result = await db.execute(select(User).where(User.email == data.email))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_active = False
    await db.commit()

    return {"message": f"User '{data.email}' has been deactivated"}
