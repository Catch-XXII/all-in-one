from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.create_user import create_user
from app.crud.get_user_by_email import get_user_by_email
from app.db.database import get_db
from app.db.schemas.user_schema import UserCreate, UserOut

router = APIRouter()


@router.post("/register", response_model=UserOut, summary="Register new user")
async def register(
    request: Request, user_in: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]
):
    existing = await get_user_by_email(db, user_in.email)
    if existing:
        return JSONResponse(status_code=200, content={"message": "Check your email"})

    try:
        body = await request.json()
        ip = (
            body.get("ip")
            or request.headers.get("x-forwarded-for", request.client.host)
            .split(",")[0]
            .strip()
        )

        location = {
            "country": body.get("country"),
            "city": body.get("city"),
            "latitude": body.get("latitude"),
            "longitude": body.get("longitude"),
        }

        user = await create_user(
            db,
            user_in,
            ip=ip,
            user_agent=request.headers.get("user-agent"),
            location=location,
        )
        return (
            user
            if user
            else JSONResponse(status_code=200, content={"message": "Check your email"})
        )

    except (IntegrityError, SQLAlchemyError):
        await db.rollback()
        return JSONResponse(status_code=200, content={"message": "Check your email"})
