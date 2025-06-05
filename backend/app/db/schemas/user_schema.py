from datetime import datetime

from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class LocationOut(BaseModel):
    country: str | None
    city: str | None
    created_at: datetime

    model_config = SettingsConfigDict(from_attributes=True)


class UserOut(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    last_login_at: datetime | None
    total_requests: int
    last_ip: str | None
    last_user_agent: str | None
    locations: list[LocationOut] = []

    model_config = SettingsConfigDict(from_attributes=True)
