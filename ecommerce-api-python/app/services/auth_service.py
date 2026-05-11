from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.exceptions.custom import MailYaRegistradoException
from app.models.role import Role
from app.models.usuario import Usuario
from app.schemas.auth import AuthResponse, LoginRequest, RegisterRequest
from app.security.jwt import generate_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def register(request: RegisterRequest, db: Session) -> AuthResponse:
    if db.query(Usuario).filter(Usuario.mail == request.mail).first():
        raise MailYaRegistradoException()

    usuario = Usuario(
        nombre_usuario=request.nombreUsuario,
        nombre=request.nombre,
        apellido=request.apellido,
        mail=request.mail,
        contrasena=pwd_context.hash(request.password),
        role=Role.USER,
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return AuthResponse(
        mensaje="Usuario registrado exitosamente",
        nombreUsuario=usuario.nombre_usuario,
        token=None,
    )


def authenticate(request: LoginRequest, db: Session) -> AuthResponse:
    usuario = db.query(Usuario).filter(Usuario.mail == request.mail).first()
    if not usuario or not pwd_context.verify(request.password, usuario.contrasena):
        raise ValueError("Credenciales inválidas")

    roles = {f"ROLE_{usuario.role.value}"}
    token = generate_token(usuario.mail, roles)

    return AuthResponse(
        mensaje="Ingreso exitoso",
        nombreUsuario=usuario.nombre_usuario,
        token=token,
    )
