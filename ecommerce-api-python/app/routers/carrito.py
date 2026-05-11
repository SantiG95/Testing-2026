from typing import List

from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.carrito import CarritoCreateDTO, CarritoDTO, ProductoCarritoInputDTO
from app.security.dependencies import get_current_user
from app.services import carrito_service

router = APIRouter(prefix="/api/carrito", tags=["Carrito"])


@router.get("", response_model=List[CarritoDTO])
def get_all_carritos(
    db: Session = Depends(get_db),
    _: Usuario = Depends(get_current_user),
):
    return carrito_service.get_all_carritos(db)


@router.get("/{id}", response_model=CarritoDTO)
def get_carrito_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: Usuario = Depends(get_current_user),
):
    return carrito_service.get_carrito_by_id(id, db)


@router.post("", response_model=CarritoDTO, status_code=status.HTTP_201_CREATED)
def create_carrito(
    dto: CarritoCreateDTO,
    db: Session = Depends(get_db),
    _: Usuario = Depends(get_current_user),
):
    return carrito_service.save_carrito(dto, db)


@router.post("/{id_carrito}/productos", response_model=CarritoDTO)
def add_producto(
    id_carrito: int,
    dto: ProductoCarritoInputDTO,
    db: Session = Depends(get_db),
    _: Usuario = Depends(get_current_user),
):
    return carrito_service.add_producto_to_carrito(id_carrito, dto, db)


@router.put("/{id_carrito}/productos/{id_producto}/reduce", response_model=CarritoDTO)
def reduce_producto(
    id_carrito: int,
    id_producto: int,
    cantidad: int = Query(..., gt=0),
    db: Session = Depends(get_db),
    _: Usuario = Depends(get_current_user),
):
    return carrito_service.reduce_cantidad_producto(id_carrito, id_producto, cantidad, db)


@router.delete("/{id_carrito}/productos/{id_producto}", response_model=CarritoDTO)
def delete_producto(
    id_carrito: int,
    id_producto: int,
    db: Session = Depends(get_db),
    _: Usuario = Depends(get_current_user),
):
    return carrito_service.delete_producto_in_carrito(id_carrito, id_producto, db)


@router.delete("/{id_carrito}/productos", response_model=CarritoDTO)
def vaciar_carrito(
    id_carrito: int,
    db: Session = Depends(get_db),
    _: Usuario = Depends(get_current_user),
):
    return carrito_service.vaciar_carrito(id_carrito, db)


@router.post("/{id}/checkout", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def checkout(
    id: int,
    _: Usuario = Depends(get_current_user),
):
    return Response(
        content='{"mensaje": "Checkout no implementado", "codigo": 501}',
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        media_type="application/json",
    )
