from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from redis import asyncio as aioredis

from app.core.config import settings


async def setup_rate_limiter():
    """Initialize the rate limiter with Redis"""
    redis = aioredis.from_url(
        settings.redis_url,
        encoding="utf-8",
        decode_responses=True,
    )
    await FastAPILimiter.init(redis)


# Create rate limit decorators for different scenarios
def default_rate_limit():
    return RateLimiter(times=100, seconds=60)


def strict_rate_limit():
    return RateLimiter(times=5, seconds=60)


def login_rate_limit():
    return RateLimiter(times=5, seconds=300)


def register_rate_limit():
    return RateLimiter(times=5, seconds=300)
