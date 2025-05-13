from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password
from app.db.models.user import User
from app.db.schemas.user_schema import UserCreate


async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    hashed_pw = hash_password(user_in.password)
    user = User(email=str(user_in.email), hashed_password=hashed_pw)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_user_by_email(db: AsyncSession, email: EmailStr) -> User | None:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()
