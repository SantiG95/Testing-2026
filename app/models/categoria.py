from sqlalchemy import Column, BigInteger, String
from app.database import Base


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(100), unique=True, nullable=False)
