from datetime import UTC, datetime

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password
from app.crud.user_location import insert_user_location
from app.db.models.user import User


async def create_user(
    db: AsyncSession,
    user_in,
    ip: str | None = None,
    user_agent: str | None = None,
    location: dict | None = None,
):
    hashed_pw = hash_password(user_in.password)

    user = User(
        email=user_in.email,
        hashed_password=hashed_pw,
        is_active=True,
        is_superuser=False,
        created_at=datetime.now(UTC),
        last_login_at=datetime.now(UTC),
        last_ip=ip,
        last_user_agent=user_agent,
    )

    try:
        db.add(user)
        await db.flush()  # ID is now available

        if location:
            await insert_user_location(
                db,
                ip=ip,
                country=location.get("country"),
                city=location.get("city"),
                latitude=location.get("latitude"),
                longitude=location.get("longitude"),
                user_id=user.id,
            )

        await db.commit()
        await db.refresh(user)
        return user

    except IntegrityError:
        await db.rollback()
        return None
    except SQLAlchemyError:
        await db.rollback()
        return None
