import asyncio
import socket

from hypercorn.asyncio import serve
from hypercorn.config import Config

from app.core.config import settings
from app.main import app


def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

if is_port_in_use(8000):
    print("Port 8000 already in use. Try `lsof -i :8000` to find the culprit.")
    exit(1)

if __name__ == "__main__":
    config = Config()
    config.bind = [f"{settings.API_HOST}:{settings.API_PORT}"]
    config.reload = True
    config.loglevel = "debug"
    asyncio.run(serve(app=app, config=config))
