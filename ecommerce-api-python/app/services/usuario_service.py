from typing import List

from sqlalchemy.orm import Session

from app.exceptions.custom import UsuarioNotFoundException
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioDTO, UsuarioUpdateDTO


def _to_dto(usuario: Usuario) -> UsuarioDTO:
    return UsuarioDTO(
        id=usuario.id,
        nombreUsuario=usuario.nombre_usuario,
        mail=usuario.mail,
        nombre=usuario.nombre,
        apellido=usuario.apellido,
        role=usuario.role.value if usuario.role else None,
    )


def get_all_usuarios(db: Session) -> List[UsuarioDTO]:
    return [_to_dto(u) for u in db.query(Usuario).all()]


def get_usuario_by_id(id: int, db: Session) -> UsuarioDTO:
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise UsuarioNotFoundException(id)
    return _to_dto(usuario)


def delete_usuario_by_id(id: int, db: Session) -> None:
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise UsuarioNotFoundException(id)
    db.delete(usuario)
    db.commit()


def update_usuario(id: int, dto: UsuarioUpdateDTO, db: Session) -> UsuarioDTO:
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise UsuarioNotFoundException(id)

    if dto.nombre is not None:
        usuario.nombre = dto.nombre
    if dto.apellido is not None:
        usuario.apellido = dto.apellido
    if dto.mail is not None:
        usuario.mail = dto.mail

    db.commit()
    db.refresh(usuario)
    return _to_dto(usuario)
