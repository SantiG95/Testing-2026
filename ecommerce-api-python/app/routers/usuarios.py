from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioDTO, UsuarioUpdateDTO
from app.security.dependencies import require_admin
from app.services import usuario_service

router = APIRouter(prefix="/api/usuarios", tags=["Usuarios"])


@router.get("", response_model=List[UsuarioDTO])
def get_all_usuarios(
    db: Session = Depends(get_db),
    _: Usuario = Depends(require_admin),
):
    return usuario_service.get_all_usuarios(db)


@router.get("/{id}", response_model=UsuarioDTO)
def get_usuario_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: Usuario = Depends(require_admin),
):
    return usuario_service.get_usuario_by_id(id, db)


@router.put("/{id}", response_model=UsuarioDTO)
def update_usuario(
    id: int,
    dto: UsuarioUpdateDTO,
    db: Session = Depends(get_db),
    _: Usuario = Depends(require_admin),
):
    return usuario_service.update_usuario(id, dto, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_usuario(
    id: int,
    db: Session = Depends(get_db),
    _: Usuario = Depends(require_admin),
):
    usuario_service.delete_usuario_by_id(id, db)
