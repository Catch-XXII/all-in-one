from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps.get_current_user import get_current_user
from app.db.database import get_db
from app.db.models.user import User
from app.db.models.user_locations import UserLocation
from app.db.schemas.user_schema import UserOut

router = APIRouter()


@router.get("/whoami", response_model=UserOut)
async def who_am_i(
        current_user: Annotated[User, Depends(get_current_user)],
        db: Annotated[AsyncSession, Depends(get_db)],
):
    """
    Get current user information.
    Returns basic user information for the authenticated user.
    """
    recent_location_limit = 3

    # Get user's recent locations
    result = await db.execute(
        select(UserLocation)
        .where(UserLocation.user_id == current_user.id)
        .order_by(UserLocation.created_at.desc())
        .limit(recent_location_limit)
    )
    locations = result.scalars().all()

    # Add locations to a user object
    current_user.locations = locations
    return current_user
