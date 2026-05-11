from typing import List, Optional
from pydantic import BaseModel, Field


class ProductoDTO(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(..., min_length=3, max_length=255)
    descripcion: str = Field(..., min_length=10, max_length=1000)
    precio: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    foto: Optional[str] = None
    categorias: List[str] = Field(..., min_length=1)

    model_config = {"from_attributes": True}


class ProductoUpdateDTO(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=255)
    descripcion: Optional[str] = Field(None, min_length=10, max_length=1000)
    precio: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    foto: Optional[str] = None
    categorias: Optional[List[str]] = None


class ProductoEliminadoDTO(BaseModel):
    id: int
    nombre: str


class CategoriaDTO(BaseModel):
    id: int
    nombre: str

    model_config = {"from_attributes": True}
