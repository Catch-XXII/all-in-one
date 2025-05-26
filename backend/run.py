import asyncio
import socket
import subprocess
import sys

from hypercorn.asyncio import serve
from hypercorn.config import Config
from redis import asyncio as aioredis

from app.core.config import settings
from app.main import app


async def wait_for_redis(max_retries=10, delay=2):
    for attempt in range(max_retries):
        try:
            redis = aioredis.from_url(
                settings.redis_url,
                encoding="utf-8",
                decode_responses=True,
            )
            pong = await redis.ping()
            if pong:
                print(f"✅ Redis is running at {settings.redis_url}")
                return
        except Exception:
            if attempt == 0:
                print("🚨 Redis not reachable. Attempting to start Redis via brew...")
                try:
                    subprocess.run(["brew", "services", "start", "redis"], check=True)
                    print("🚀 brew services start redis executed.")
                except subprocess.CalledProcessError as brew_err:
                    print("❌ Failed to start Redis via brew.")
                    print("🔧", brew_err)
                    sys.exit(1)

            print(f"🔄 Waiting for Redis... attempt {attempt + 1}/{max_retries}")
            await asyncio.sleep(delay)

    print("❌ Redis is NOT reachable after retries. Exiting.")
    sys.exit(1)


def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0


if is_port_in_use(8000):
    print("❌ Port 8000 already in use. Try `lsof -i :8000` to find the culprit.")
    sys.exit(1)


if __name__ == "__main__":
    config = Config()
    config.bind = [f"{settings.API_HOST}:{settings.API_PORT}"]
    config.reload = True
    config.loglevel = "debug"

    asyncio.run(wait_for_redis())
    asyncio.run(serve(app=app, config=config))
