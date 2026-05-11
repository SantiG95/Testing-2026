class ProductoNotFoundException(Exception):
    def __init__(self, mensaje: str = "Producto no encontrado"):
        self.mensaje = mensaje
        super().__init__(mensaje)


class UsuarioNotFoundException(Exception):
    def __init__(self, id: int = None):
        self.mensaje = f"Usuario no encontrado con id: {id}" if id else "Usuario no encontrado"
        super().__init__(self.mensaje)


class MailYaRegistradoException(Exception):
    def __init__(self):
        self.mensaje = "El mail ya existe en la base de datos"
        super().__init__(self.mensaje)


class PrecioNegativoException(Exception):
    def __init__(self):
        self.mensaje = "El precio no puede ser negativo"
        super().__init__(self.mensaje)
