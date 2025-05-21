from pydantic import BaseModel, EmailStr
from pydantic_settings import SettingsConfigDict


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int
    is_active: bool

    model_config = SettingsConfigDict(from_attributes=True)
