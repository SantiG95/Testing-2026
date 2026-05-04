package com.uade.tpo.e_commerce3.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.*;

import com.uade.tpo.e_commerce3.dto.ValidationErrorResponse;


// Anotación que indica que esta clase manejará excepciones de forma global para todos los controladores.
@ControllerAdvice
public class GlobalExceptionHandler {

    // Maneja errores de validación de Bean Validation (@Valid)
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ValidationErrorResponse> manejarErroresValidacion(MethodArgumentNotValidException ex) {
        ValidationErrorResponse response = ValidationErrorResponse.builder()
                .mensaje("Error de validación en la solicitud")
                .codigo(HttpStatus.BAD_REQUEST.value())
                .build();
        
        ex.getBindingResult().getFieldErrors().forEach(error ->
            response.getErrores().put(error.getField(), error.getDefaultMessage())
        );
        
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(response);
    }

    // Anotación que indica que este método manejará las excepciones de tipo ProductoNotFoundException.
    @ExceptionHandler(ProductoNotFoundException.class)
    // Este método se ejecuta cuando se lanza una ProductoNotFoundException.
    public ResponseEntity<String> manejarProductoNoEncontrado(ProductoNotFoundException ex) {

        // Devuelve una respuesta con el código de estado HTTP 404 (Not Found) y un cuerpo con el mensaje "Producto no encontrado :)"
        //representa la respuesta HTTP completa que se envía desde tu controlador al cliente (navegador, aplicación móvil, etc.).
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(ex.getMessage());
        //not_found es el código de error
        //body va el json con el mensaje de error
        
    }

    @ExceptionHandler(UsuarioNotFoundException.class)
    public ResponseEntity<String> usuarioNotFound(UsuarioNotFoundException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(ex.getMessage());
    }

    @ExceptionHandler(PrecioNegativoException.class)
    public ResponseEntity<String> manejarPrecioNegativo(PrecioNegativoException ex) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(ex.getMessage());
    }

    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<String> manejarArgumentoInvalido(IllegalArgumentException ex) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(ex.getMessage());
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> manejarErroresGenerales(Exception ex) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Error interno: " + ex.getMessage());
    }

    @ExceptionHandler(MailYaRegistradoException.class)
    public ResponseEntity<String> mailYaRegistrado(MailYaRegistradoException ex) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(ex.getMessage());
    }

    
}
