from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int
    is_active: bool

    model_config = SettingsConfigDict(from_attributes=True)
