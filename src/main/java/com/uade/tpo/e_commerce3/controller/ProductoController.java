package com.uade.tpo.e_commerce3.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.uade.tpo.e_commerce3.dto.ApiResponse;
import com.uade.tpo.e_commerce3.dto.ProductoDTO;
import com.uade.tpo.e_commerce3.dto.ProductoEliminadoDTO;
import com.uade.tpo.e_commerce3.model.Categoria;
import com.uade.tpo.e_commerce3.service.ProductoService;

import jakarta.validation.Valid;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestParam;



@RestController
// para acceder a este controlador, la URL base será /api/productos
@RequestMapping("/api/productos")
public class ProductoController {

    @Autowired
    private ProductoService productoService;

    //http://localhost:8080/api/productos -> devuelve la lista de productos
    @GetMapping
    public ResponseEntity<List<ProductoDTO>> getAllProductos() {
        List<ProductoDTO> productos = productoService.getAllProductos();
        return new ResponseEntity<>(productos, HttpStatus.OK);
    }

    @GetMapping("/categorias")
    public ResponseEntity<List<Categoria>> getCategorias() {
        List<Categoria> categorias = productoService.getAllCategorias();
        return new ResponseEntity<>(categorias, HttpStatus.OK);
    }
    

    //http://localhost:8080/api/productos/1 -> devuelve el producto con id 1
    @GetMapping("/{id}")
    public ResponseEntity<ProductoDTO> getProductoById(@PathVariable Long id) {
        ProductoDTO productoDTO = productoService.getProductoById(id);

        // Se crea una nueva instancia de ResponseEntity, pasando el producto encontrado como cuerpo de la respuesta
        // y HttpStatus.OK (código 200) como estado de la respuesta.

        //ResponseEntity es una clase que representa toda la respuesta HTTP: código de estado, encabezados y cuerpo.
        //devuelve una promesa en el cuerpo los datos del producto, y un codigo de estado 200 (OK)
        // el cuerpo es un json productos -> json
        return new ResponseEntity<ProductoDTO>(productoDTO, HttpStatus.OK);
    }

    // del http://localhost:8080/api/productos/1 -> elimina el producto con id 1
    @DeleteMapping("/{id}")
    public ResponseEntity<ApiResponse<ProductoEliminadoDTO>> deleteProducto(@PathVariable Long id) {
        ProductoEliminadoDTO productoEliminado = productoService.deleteProductoById(id);
        ApiResponse<ProductoEliminadoDTO> response = ApiResponse.<ProductoEliminadoDTO>builder()
            .mensaje("El producto " + productoEliminado.getNombre() + " fue eliminado exitosamente")
            .data(productoEliminado)
            .build();
        return new ResponseEntity<>(response, HttpStatus.OK);
    }

    /*http://localhost:8080/api/productos -> crea un nuevo producto con los datos enviados en el cuerpo 
     de la petición*/

    @PostMapping
    public ResponseEntity<ApiResponse<ProductoDTO>> saveProducto(@Valid @RequestBody ProductoDTO productoDTO) {
        ProductoDTO nuevoProducto = productoService.saveProducto(productoDTO);
        ApiResponse<ProductoDTO> response = ApiResponse.<ProductoDTO>builder()
            .mensaje("El producto " + nuevoProducto.getNombre() + " fue creado exitosamente")
            .data(nuevoProducto)
            .build();
        return new ResponseEntity<>(response, HttpStatus.CREATED);
    }
    
    @PutMapping("/{id}")
    public ResponseEntity<ApiResponse<ProductoDTO>> updateProducto(@PathVariable Long id, @Valid @RequestBody ProductoDTO productoDTO) {
        ProductoDTO productoActualizado = productoService.updateProducto(id, productoDTO);
        ApiResponse<ProductoDTO> response = ApiResponse.<ProductoDTO>builder()
            .mensaje("El producto " + productoActualizado.getNombre() + " fue actualizado exitosamente")
            .data(productoActualizado)
            .build();
        return new ResponseEntity<>(response, HttpStatus.OK);
    }

    @PutMapping("/{id}/stock")
    public ResponseEntity<ApiResponse<ProductoDTO>> updateStock(@PathVariable Long id, @RequestParam int cantidad) {
        ProductoDTO productoActualizado = productoService.updateStock(id, cantidad);
        ApiResponse<ProductoDTO> response = ApiResponse.<ProductoDTO>builder()
            .mensaje("El stock del producto " + productoActualizado.getNombre() + " fue actualizado a " + productoActualizado.getStock())
            .data(productoActualizado)
            .build();
        return new ResponseEntity<>(response, HttpStatus.OK);
    }
}
