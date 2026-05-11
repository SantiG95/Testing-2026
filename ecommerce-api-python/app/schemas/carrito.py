from typing import List, Optional
from pydantic import BaseModel, Field


class ProductoCarritoInputDTO(BaseModel):
    productoId: int = Field(..., gt=0)
    cantidad: int = Field(..., gt=0, le=1000)


class ProductoCarritoDTO(BaseModel):
    id: Optional[int] = None
    productoId: int
    nombreProducto: Optional[str] = None
    cantidad: int
    precioUnitario: Optional[float] = None

    model_config = {"from_attributes": True}


class CarritoCreateDTO(BaseModel):
    usuarioId: int


class CarritoDTO(BaseModel):
    id: Optional[int] = None
    usuarioId: int
    productos: List[ProductoCarritoDTO] = []
    total: float = 0.0

    model_config = {"from_attributes": True}
