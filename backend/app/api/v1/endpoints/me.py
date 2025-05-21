from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.deps.auth_deps import get_current_user
from app.db.models.user import User
from app.db.schemas.user_schema import UserOut

router = APIRouter()



@router.get("/me", response_model=UserOut)
async def get_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
