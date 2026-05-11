from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.exceptions.custom import (
    MailYaRegistradoException,
    PrecioNegativoException,
    ProductoNotFoundException,
    UsuarioNotFoundException,
)


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        errores = {}
        for error in exc.errors():
            campo = ".".join(str(loc) for loc in error["loc"] if loc != "body")
            errores[campo] = error["msg"]
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"mensaje": "Error de validación", "codigo": 400, "errores": errores},
        )

    @app.exception_handler(ProductoNotFoundException)
    async def producto_not_found_handler(request: Request, exc: ProductoNotFoundException):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"mensaje": exc.mensaje, "codigo": 404},
        )

    @app.exception_handler(UsuarioNotFoundException)
    async def usuario_not_found_handler(request: Request, exc: UsuarioNotFoundException):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"mensaje": exc.mensaje, "codigo": 404},
        )

    @app.exception_handler(MailYaRegistradoException)
    async def mail_ya_registrado_handler(request: Request, exc: MailYaRegistradoException):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"mensaje": exc.mensaje, "codigo": 400},
        )

    @app.exception_handler(PrecioNegativoException)
    async def precio_negativo_handler(request: Request, exc: PrecioNegativoException):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"mensaje": exc.mensaje, "codigo": 400},
        )

    @app.exception_handler(ValueError)
    async def value_error_handler(request: Request, exc: ValueError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"mensaje": str(exc), "codigo": 400},
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"mensaje": "Error interno del servidor", "codigo": 500},
        )
