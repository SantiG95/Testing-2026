from typing import Optional
from pydantic import BaseModel, EmailStr


class UsuarioDTO(BaseModel):
    id: Optional[int] = None
    nombreUsuario: Optional[str] = None
    mail: Optional[EmailStr] = None
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    role: Optional[str] = None

    model_config = {"from_attributes": True}


class UsuarioUpdateDTO(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    mail: Optional[EmailStr] = None
