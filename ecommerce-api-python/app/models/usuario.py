from sqlalchemy import Column, BigInteger, String, Enum
from app.database import Base
from app.models.role import Role


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre_usuario = Column("nombre_usuario", String(50), nullable=False)
    nombre = Column(String(100))
    apellido = Column(String(100))
    mail = Column(String(255), unique=True, index=True)
    contrasena = Column(String(255))
    role = Column(Enum(Role), default=Role.USER)
