from datetime import UTC, datetime, timedelta

from jose import JWTError, jwt

from app.core.config import settings

if len(settings.JWT_SECRET_KEY) < 32:
    raise ValueError("JWT_SECRET_KEY must be at least 32 characters long for security.")

if settings.JWT_ALGORITHM not in {"HS256", "RS256"}:
    raise ValueError(f"Unsupported JWT algorithm: {settings.JWT_ALGORITHM}")


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    create a JSON Web Token (JWT) with an expiration.

    Args:
        data (dict): The data/payload to include in the token.
        expires_delta (timedelta | None, optional):
        Duration for which the token is valid.
            if not provided, it defaults to a value defined in settings.

    Returns:
        str: The encoded JWT string.

    Raises:
        ValueError: If input data or configuration values are invalid.
        RuntimeError: If JWT encoding fails.
    """
    # Validate input
    if not isinstance(data, dict):
        raise ValueError("The `data` argument must be a dictionary.")
    if expires_delta is not None and not isinstance(expires_delta, timedelta):
        raise ValueError("The `expires_delta` argument must be a `timedelta` object.")

    # Fallback expiration if isn't provided
    default_expire_minutes = 15
    expire = datetime.now(UTC) + (
            expires_delta
            or timedelta(
        minutes=getattr(
            settings, "ACCESS_TOKEN_EXPIRE_MINUTES", default_expire_minutes
        )
    )
    )

    # Add standard claims to the payload
    to_encode = data.copy()
    to_encode.update({"exp": expire, "iat": datetime.now(UTC), "sub": "access_token"})

    # Securely encode the token
    try:
        encoded_jwt = jwt.encode(
            to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
        )
    except JWTError as e:
        raise RuntimeError(f"Failed to encode JWT: {e}") from e

    return encoded_jwt
