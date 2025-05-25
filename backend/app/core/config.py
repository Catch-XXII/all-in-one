from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    API_HOST: str
    API_PORT: int
    FRONTEND_ORIGIN: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    TITLE: str
    DESCRIPTION: str
    VERSION: str

    @computed_field
    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # New structure for getting settings v2.x
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
