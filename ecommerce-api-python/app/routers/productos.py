from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.common import ApiResponse
from app.schemas.producto import CategoriaDTO, ProductoDTO, ProductoEliminadoDTO, ProductoUpdateDTO
from app.security.dependencies import get_current_user, require_admin
from app.services import producto_service

router = APIRouter(prefix="/api/productos", tags=["Productos"])


@router.get("", response_model=List[ProductoDTO])
def get_all_productos(db: Session = Depends(get_db)):
    return producto_service.get_all_productos(db)


@router.get("/categorias", response_model=List[CategoriaDTO])
def get_all_categorias(db: Session = Depends(get_db)):
    return producto_service.get_all_categorias(db)


@router.get("/{id}", response_model=ProductoDTO)
def get_producto_by_id(id: int, db: Session = Depends(get_db)):
    return producto_service.get_producto_by_id(id, db)


@router.post("", response_model=ApiResponse[ProductoDTO])
def create_producto(
    dto: ProductoDTO,
    db: Session = Depends(get_db),
    _: Usuario = Depends(require_admin),
):
    producto = producto_service.save_producto(dto, db)
    return ApiResponse(mensaje="Producto creado exitosamente", codigo=201, data=producto)


@router.put("/{id}", response_model=ApiResponse[ProductoDTO])
def update_producto(
    id: int,
    dto: ProductoUpdateDTO,
    db: Session = Depends(get_db),
    _: Usuario = Depends(require_admin),
):
    producto = producto_service.update_producto(id, dto, db)
    return ApiResponse(mensaje="Producto actualizado exitosamente", codigo=200, data=producto)


@router.put("/{id}/stock", response_model=ApiResponse[ProductoDTO])
def update_stock(
    id: int,
    cantidad: int = Query(..., ge=0),
    db: Session = Depends(get_db),
    _: Usuario = Depends(require_admin),
):
    producto = producto_service.update_stock(id, cantidad, db)
    return ApiResponse(mensaje="Stock actualizado exitosamente", codigo=200, data=producto)


@router.delete("/{id}", response_model=ApiResponse[ProductoEliminadoDTO])
def delete_producto(
    id: int,
    db: Session = Depends(get_db),
    _: Usuario = Depends(require_admin),
):
    eliminado = producto_service.delete_producto_by_id(id, db)
    return ApiResponse(mensaje="Producto eliminado exitosamente", codigo=200, data=eliminado)
