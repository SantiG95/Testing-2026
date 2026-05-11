from sqlalchemy import Column, BigInteger, String, Float, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

productos_categorias = Table(
    "productos_categorias",
    Base.metadata,
    Column("producto_id", BigInteger, ForeignKey("productos.id")),
    Column("categoria_id", BigInteger, ForeignKey("categorias.id")),
)


class Producto(Base):
    __tablename__ = "productos"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String(1000))
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    foto = Column(String(500))

    categorias = relationship("Categoria", secondary=productos_categorias, lazy="select")
    productos_carrito = relationship(
        "ProductoCarrito", back_populates="producto", cascade="all, delete-orphan"
    )
