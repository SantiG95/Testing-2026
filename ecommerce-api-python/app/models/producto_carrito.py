from sqlalchemy import Column, BigInteger, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class ProductoCarrito(Base):
    __tablename__ = "producto_carrito"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    carrito_id = Column(BigInteger, ForeignKey("carrito.id"))
    producto_id = Column(BigInteger, ForeignKey("productos.id"))
    cantidad_producto = Column(Integer)

    carrito = relationship("Carrito", back_populates="productos")
    producto = relationship("Producto", back_populates="productos_carrito")
