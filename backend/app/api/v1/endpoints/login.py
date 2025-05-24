from datetime import UTC, datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.jwt import create_access_token
from app.core.security import verify_password
from app.crud.get_user_by_email import get_user_by_email
from app.db.database import get_db
from app.db.models.user import User
from app.db.schemas.token_schema import Token

router = APIRouter()


@router.post(
    "/login", response_model=Token, summary="Authenticate user and return JWT token"
)
async def login(
    request: Request,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    user: User | None = await get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    user.last_login_at = datetime.now(UTC)
    user.last_ip = request.client.host
    user.last_user_agent = request.headers.get("user-agent")

    await db.commit()

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
