from typing import List

from sqlalchemy.orm import Session

from app.exceptions.custom import ProductoNotFoundException
from app.models.carrito import Carrito
from app.models.producto import Producto
from app.models.producto_carrito import ProductoCarrito
from app.schemas.carrito import CarritoCreateDTO, CarritoDTO, ProductoCarritoDTO, ProductoCarritoInputDTO


def _to_item_dto(item: ProductoCarrito) -> ProductoCarritoDTO:
    return ProductoCarritoDTO(
        id=item.id,
        productoId=item.producto_id,
        nombreProducto=item.producto.nombre,
        cantidad=item.cantidad_producto,
        precioUnitario=item.producto.precio,
    )


def _to_carrito_dto(carrito: Carrito) -> CarritoDTO:
    items = [_to_item_dto(i) for i in carrito.productos]
    total = sum(i.precioUnitario * i.cantidad for i in items)
    return CarritoDTO(
        id=carrito.id,
        usuarioId=carrito.usuario_id,
        productos=items,
        total=total,
    )


def get_all_carritos(db: Session) -> List[CarritoDTO]:
    return [_to_carrito_dto(c) for c in db.query(Carrito).all()]


def get_carrito_by_id(id: int, db: Session) -> CarritoDTO:
    carrito = db.query(Carrito).filter(Carrito.id == id).first()
    if not carrito:
        raise ValueError(f"Carrito no encontrado con id: {id}")
    return _to_carrito_dto(carrito)


def save_carrito(dto: CarritoCreateDTO, db: Session) -> CarritoDTO:
    carrito = Carrito(usuario_id=dto.usuarioId)
    db.add(carrito)
    db.commit()
    db.refresh(carrito)
    return _to_carrito_dto(carrito)


def add_producto_to_carrito(id_carrito: int, dto: ProductoCarritoInputDTO, db: Session) -> CarritoDTO:
    carrito = db.query(Carrito).filter(Carrito.id == id_carrito).first()
    if not carrito:
        raise ValueError(f"Carrito no encontrado con id: {id_carrito}")

    if dto.cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a 0")

    producto = db.query(Producto).filter(Producto.id == dto.productoId).first()
    if not producto:
        raise ProductoNotFoundException(f"Producto no encontrado con id: {dto.productoId}")

    if producto.stock < dto.cantidad:
        raise ValueError("Stock insuficiente")

    item_existente = next(
        (i for i in carrito.productos if i.producto_id == dto.productoId), None
    )

    if item_existente:
        if item_existente.cantidad_producto + dto.cantidad > producto.stock:
            raise ValueError("No hay suficiente stock")
        item_existente.cantidad_producto += dto.cantidad
    else:
        nuevo_item = ProductoCarrito(
            carrito_id=carrito.id,
            producto_id=dto.productoId,
            cantidad_producto=dto.cantidad,
        )
        db.add(nuevo_item)
        carrito.productos.append(nuevo_item)

    db.commit()
    db.refresh(carrito)
    return _to_carrito_dto(carrito)


def delete_producto_in_carrito(id_carrito: int, id_producto: int, db: Session) -> CarritoDTO:
    carrito = db.query(Carrito).filter(Carrito.id == id_carrito).first()
    if not carrito:
        raise ValueError(f"Carrito no encontrado con id: {id_carrito}")

    item = next((i for i in carrito.productos if i.producto_id == id_producto), None)
    if item:
        db.delete(item)
        db.commit()
        db.refresh(carrito)

    return _to_carrito_dto(carrito)


def reduce_cantidad_producto(id_carrito: int, id_producto: int, cantidad: int, db: Session) -> CarritoDTO:
    carrito = db.query(Carrito).filter(Carrito.id == id_carrito).first()
    if not carrito:
        raise ValueError(f"Carrito no encontrado con id: {id_carrito}")

    item = next((i for i in carrito.productos if i.producto_id == id_producto), None)
    if not item:
        raise ValueError("Producto no encontrado en el carrito")

    if cantidad <= 0:
        raise ValueError("La cantidad a eliminar debe ser mayor a 0")

    if cantidad > item.cantidad_producto:
        raise ValueError(
            f"No puedes eliminar {cantidad} productos. El carrito solo tiene {item.cantidad_producto}"
        )

    if cantidad == item.cantidad_producto:
        db.delete(item)
    else:
        item.cantidad_producto -= cantidad

    db.commit()
    db.refresh(carrito)
    return _to_carrito_dto(carrito)


def vaciar_carrito(id_carrito: int, db: Session) -> CarritoDTO:
    carrito = db.query(Carrito).filter(Carrito.id == id_carrito).first()
    if not carrito:
        raise ValueError(f"Carrito no encontrado con id: {id_carrito}")

    for item in list(carrito.productos):
        db.delete(item)

    db.commit()
    db.refresh(carrito)
    return _to_carrito_dto(carrito)
