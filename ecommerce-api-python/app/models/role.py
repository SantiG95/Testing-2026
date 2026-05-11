import enum


class Role(str, enum.Enum):
    USER = "USER"
    ADMIN = "ADMIN"
    VENDEDOR = "VENDEDOR"
