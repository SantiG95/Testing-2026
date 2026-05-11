from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.exceptions.handlers import register_exception_handlers
from app.routers import auth, carrito, productos, usuarios

import app.models  # noqa: F401 — registra todos los modelos antes de crear tablas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce API",
    description="API REST de e-commerce con autenticación JWT",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)

app.include_router(auth.router)
app.include_router(productos.router)
app.include_router(carrito.router)
app.include_router(usuarios.router)


@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "mensaje": "E-Commerce API funcionando"}
