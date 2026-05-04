package com.uade.tpo.e_commerce3.controller;

import java.util.List;

import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.uade.tpo.e_commerce3.dto.CarritoDTO;
import com.uade.tpo.e_commerce3.dto.ProductoCarritoDTO;
import com.uade.tpo.e_commerce3.model.Carrito;
import com.uade.tpo.e_commerce3.service.CarritoService;


@RestController
@RequestMapping("/api/carrito")
public class CarritoController {
    
    @Autowired
    private CarritoService carritoService;

    @GetMapping
    public ResponseEntity<List<CarritoDTO>> getAllCarritos() {
        List<CarritoDTO> carritos = carritoService.getAllCarritos();
        return new ResponseEntity<>(carritos, HttpStatus.OK);
    }

    @GetMapping("/{id}")
    public ResponseEntity<CarritoDTO> getCarritoById(@PathVariable Long id) {
        CarritoDTO carrito = carritoService.getCarritoById(id);
        return new ResponseEntity<>(carrito, HttpStatus.OK);
    }

    @PostMapping
    public Carrito saveCarrito(@RequestBody Carrito carrito) {
        return carritoService.saveCarrito(carrito);
    }

    @DeleteMapping("/{idCarrito}/productos/{idProducto}")
    public CarritoDTO deleteProductoInCarritoById(@PathVariable Long idCarrito, @PathVariable Long idProducto) {
        CarritoDTO carritoActualizado = carritoService.deleteProductoInCarritoById(idCarrito, idProducto);
        return carritoActualizado;
    }

    // crear deleteProductoInCarritoById
    @PutMapping("/{idCarrito}/productos/{idProducto}/reduce")
    public ResponseEntity<CarritoDTO> reduceCantidadProductoInCarrito(@PathVariable Long idCarrito, @PathVariable Long idProducto, @RequestParam Integer cantidad) {
        CarritoDTO carrito = carritoService.reduceCantidadProductoInCarritoById(idCarrito, idProducto, cantidad);
        return ResponseEntity.ok(carrito);
    }

    //vaciar carrito, eliminar todos los productos del carrito
    @DeleteMapping("/{idCarrito}/productos")
    public ResponseEntity<CarritoDTO> vaciarCarrito(@PathVariable Long idCarrito) {
        CarritoDTO carritoVacio = carritoService.vaciarCarritoById(idCarrito);
        return new ResponseEntity<>(carritoVacio, HttpStatus.OK);
    }
    //TODO: implementar checkout
    @PostMapping("/{id}/checkout")
    public ResponseEntity<String> doCheckout(@PathVariable Long id) {
        //TODO Checkout pendiente por ahora
        return new ResponseEntity<>("Funcionalidad de Checkout deshabilitada temporalmente.", HttpStatus.NOT_IMPLEMENTED);
    }

    // crear addProductoToCarrito
    @PostMapping("/{idCarrito}/productos")
    public ResponseEntity<CarritoDTO> addProductoToCarrito(@PathVariable Long idCarrito, @Valid @RequestBody ProductoCarritoDTO nuevoProducto) {
        CarritoDTO carritoActualizado = carritoService.addProductoToCarrito(idCarrito, nuevoProducto);
        return new ResponseEntity<>(carritoActualizado, HttpStatus.OK);
    }
}
