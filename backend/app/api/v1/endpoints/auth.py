from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps.auth_deps import get_current_user, require_admin
from app.core.jwt import create_access_token
from app.core.security import verify_password
from app.crud.user_crud import create_user, get_user_by_email
from app.db.database import get_db
from app.db.models.user import User
from app.db.schemas.token_schema import Token
from app.db.schemas.user_schema import UserCreate, UserOut

router = APIRouter()


@router.post("/register", response_model=UserOut)
async def register(user_in: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    existing = await get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )
    user = await create_user(db, user_in)
    return user


@router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    user: User | None = await get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=UserOut)
async def get_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@router.get("/admin-only")
async def read_admin_data(admin: Annotated[User, Depends(require_admin)]):
    return {"message": f"Hello Admin {admin.email}!"}
