from sqlalchemy import Column, BigInteger
from sqlalchemy.orm import relationship
from app.database import Base


class Carrito(Base):
    __tablename__ = "carrito"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    usuario_id = Column(BigInteger, nullable=False)

    productos = relationship(
        "ProductoCarrito", back_populates="carrito", cascade="all, delete-orphan"
    )
