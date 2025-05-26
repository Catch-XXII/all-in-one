from datetime import UTC, datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.jwt import create_access_token
from app.core.rate_limiter import login_rate_limit
from app.core.security import verify_password
from app.crud.get_user_by_email import get_user_by_email
from app.crud.user_location import insert_user_location
from app.db.database import get_db
from app.db.models.user import User
from app.db.schemas.token_schema import Token

router = APIRouter()


@router.post(
    "/login",
    response_model=Token,
    summary="Authenticate user and return JWT token",
    dependencies=[Depends(login_rate_limit())],
)
async def login(
    request: Request,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    form = await request.form()
    ip = (
        form.get("ip")
        or request.headers.get("x-forwarded-for", request.client.host)
        .split(",")[0]
        .strip()
    )
    location = {
        "country": form.get("country"),
        "city": form.get("city"),
        "latitude": float(form.get("latitude")) if form.get("latitude") else None,
        "longitude": float(form.get("longitude")) if form.get("longitude") else None,
    }

    user: User | None = await get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    user.last_login_at = datetime.now(UTC)
    user.last_ip = ip
    user.last_user_agent = request.headers.get("user-agent")

    try:
        await insert_user_location(
            db,
            ip=ip,
            country=location["country"],
            city=location["city"],
            latitude=location["latitude"],
            longitude=location["longitude"],
            user_id=user.id,
        )
        await db.commit()
    except SQLAlchemyError:
        await db.rollback()

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
