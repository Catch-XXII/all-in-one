from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.user_crud import create_user, get_user_by_email
from app.db.database import get_db
from app.db.schemas.user_schema import UserCreate, UserOut

router = APIRouter()


@router.post("/register", response_model=UserOut, summary="Register new user")
async def register(user_in: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    existing = await get_user_by_email(db, user_in.email)
    if existing:
        return JSONResponse(status_code=200, content={"message": "Check your email"})

    user = await create_user(db, user_in)
    return user
