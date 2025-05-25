import logging

from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.user_locations import UserLocation

logger = logging.getLogger(__name__)


async def insert_user_location(
    db: AsyncSession,
    ip: str,
    country: str | None = None,
    city: str | None = None,
    latitude: float | None = None,
    longitude: float | None = None,
    user_id: int | None = None,
):
    try:
        stmt = insert(UserLocation).values(
            user_id=user_id,
            ip=ip,
            country=country,
            city=city,
            latitude=latitude,
            longitude=longitude,
        )
        await db.execute(stmt)
    except SQLAlchemyError as e:
        await db.rollback()
        logger.warning(f"Failed to insert user location: {e}")
