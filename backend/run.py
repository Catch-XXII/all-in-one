import asyncio

from hypercorn.asyncio import serve
from hypercorn.config import Config

from app.core.config import settings
from app.main import app

if __name__ == "__main__":
    config = Config()
    config.bind = [f"{settings.API_HOST}:{settings.API_PORT}"]
    config.reload = True
    config.loglevel = "debug"
    asyncio.run(serve(app=app, config=config))
