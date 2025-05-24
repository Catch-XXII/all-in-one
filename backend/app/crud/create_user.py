from datetime import UTC, datetime

from sqlalchemy.exc import IntegrityError

from app.core.security import hash_password
from app.db.models.user import User


async def create_user(db, user_in, ip=None, user_agent=None):
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
        await db.commit()
        await db.refresh(user)
        return user
    except IntegrityError:
        await db.rollback()
        return None
