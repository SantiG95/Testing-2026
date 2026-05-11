from typing import List, Optional
from pydantic import BaseModel, Field


class ProductoDTO(BaseModel):
    id: Optional[int] = None
    nombre: str
    descripcion: str
    precio: float
    stock: int
    foto: Optional[str] = None
    categorias: List[str]

    model_config = {"from_attributes": True}


class ProductoUpdateDTO(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    foto: Optional[str] = None
    categorias: List[str]


class ProductoEliminadoDTO(BaseModel):
    id: int
    nombre: str


class CategoriaDTO(BaseModel):
    id: int
    nombre: str

    model_config = {"from_attributes": True}
