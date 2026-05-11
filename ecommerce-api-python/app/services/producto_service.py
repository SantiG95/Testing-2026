from typing import List

from sqlalchemy.orm import Session

from app.exceptions.custom import ProductoNotFoundException
from app.models.categoria import Categoria
from app.models.producto import Producto
from app.schemas.producto import CategoriaDTO, ProductoDTO, ProductoEliminadoDTO, ProductoUpdateDTO


def _to_dto(producto: Producto) -> ProductoDTO:
    return ProductoDTO(
        id=producto.id,
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        precio=producto.precio,
        stock=producto.stock,
        foto=producto.foto,
        categorias=[c.nombre for c in producto.categorias],
    )


def _resolve_categorias(nombres: List[str], db: Session) -> List[Categoria]:
    resultado = []
    for nombre in nombres:
        categoria = db.query(Categoria).filter(Categoria.nombre == nombre).first()
        if not categoria:
            categoria = Categoria(nombre=nombre)
            db.add(categoria)
            db.flush()
        resultado.append(categoria)
    return resultado


def get_all_productos(db: Session) -> List[ProductoDTO]:
    productos = db.query(Producto).order_by(Producto.nombre.asc()).all()
    return [_to_dto(p) for p in productos]


def get_all_categorias(db: Session) -> List[CategoriaDTO]:
    categorias = db.query(Categoria).all()
    return [CategoriaDTO(id=c.id, nombre=c.nombre) for c in categorias]


def get_producto_by_id(id: int, db: Session) -> ProductoDTO:
    producto = db.query(Producto).filter(Producto.id == id).first()
    if not producto:
        raise ProductoNotFoundException(f"Producto no encontrado con id: {id}")
    return _to_dto(producto)


def save_producto(dto: ProductoDTO, db: Session) -> ProductoDTO:
    producto = Producto(
        nombre=dto.nombre,
        descripcion=dto.descripcion,
        precio=dto.precio,
        stock=dto.stock,
        foto=dto.foto,
    )
    producto.categorias = _resolve_categorias(dto.categorias, db)
    db.add(producto)
    db.commit()
    db.refresh(producto)
    return _to_dto(producto)


def update_producto(id: int, dto: ProductoUpdateDTO, db: Session) -> ProductoDTO:
    producto = db.query(Producto).filter(Producto.id == id).first()
    if not producto:
        raise ProductoNotFoundException(f"Producto no encontrado con id: {id}")

    if dto.nombre is not None:
        producto.nombre = dto.nombre
    if dto.descripcion is not None:
        producto.descripcion = dto.descripcion
    if dto.precio is not None:
        producto.precio = dto.precio
    if dto.stock is not None:
        producto.stock = dto.stock
    if dto.foto is not None:
        producto.foto = dto.foto
    if dto.categorias is not None:
        producto.categorias = _resolve_categorias(dto.categorias, db)

    db.commit()
    db.refresh(producto)
    return _to_dto(producto)


def update_stock(id: int, cantidad: int, db: Session) -> ProductoDTO:
    producto = db.query(Producto).filter(Producto.id == id).first()
    if not producto:
        raise ProductoNotFoundException(f"Producto no encontrado con id: {id}")
    producto.stock = cantidad
    db.commit()
    db.refresh(producto)
    return _to_dto(producto)


def delete_producto_by_id(id: int, db: Session) -> ProductoEliminadoDTO:
    producto = db.query(Producto).filter(Producto.id == id).first()
    if not producto:
        raise ProductoNotFoundException(f"Producto no encontrado con id: {id}")
    nombre = producto.nombre
    db.delete(producto)
    db.commit()
    return ProductoEliminadoDTO(id=id, nombre=nombre)
