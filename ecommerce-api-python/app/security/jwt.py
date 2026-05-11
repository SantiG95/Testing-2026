from datetime import datetime, timedelta, timezone
from typing import Optional, Set

from jose import JWTError, jwt

from app.config import settings

ALGORITHM = "HS256"


def generate_token(username: str, roles: Set[str]) -> str:
    expire = datetime.now(timezone.utc) + timedelta(milliseconds=settings.JWT_EXPIRATION)
    payload = {
        "sub": username,
        "roles": ",".join(roles),
        "iat": datetime.now(timezone.utc),
        "exp": expire,
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=ALGORITHM)


def get_username(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None


def get_roles(token: str) -> Set[str]:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[ALGORITHM])
        roles_str = payload.get("roles", "")
        return set(roles_str.split(",")) if roles_str else set()
    except JWTError:
        return set()


def validate_token(token: str) -> bool:
    try:
        jwt.decode(token, settings.JWT_SECRET, algorithms=[ALGORITHM])
        return True
    except JWTError:
        return False
