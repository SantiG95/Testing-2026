package com.uade.tpo.e_commerce3.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.util.List;
import java.util.stream.Collectors;

import com.uade.tpo.e_commerce3.model.Carrito;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class CarritoDTO {
    private Long id;
    private Long usuarioId;
    private List<ProductoCarritoDTO> productos;
    private Double total;

    public CarritoDTO(Carrito carrito) {
        this.id = carrito.getId();
        this.usuarioId = carrito.getUsuarioId();
        
        // Mapea sus propios items usando el constructor que creamos en el paso anterior
        this.productos = carrito.getProductos().stream()
                .map(ProductoCarritoDTO::new) 
                .collect(Collectors.toList());
        
        // Calcula su propio total
        this.total = this.productos.stream()
                .mapToDouble(item -> item.getPrecioUnitario() * item.getCantidad())
                .sum();
    }
}