from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.deps.get_current_user import get_current_user
from app.db.models.user import User
from app.db.schemas.user_schema import UserOut

router = APIRouter()


@router.get("/whoami", response_model=UserOut)
async def who_am_i(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
