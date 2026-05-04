package com.uade.tpo.e_commerce3.dto;

import com.uade.tpo.e_commerce3.model.ProductoCarrito;

import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ProductoCarritoDTO {
    private Long id;  // Solo lectura
    
    @NotNull(message = "El ID del producto es obligatorio")
    @Positive(message = "El ID del producto debe ser un número positivo")
    private Long productoId;
    
    private String nombreProducto;  // Solo lectura
    
    @NotNull(message = "La cantidad es obligatoria")
    @Positive(message = "La cantidad debe ser mayor a 0")
    @Max(value = 1000, message = "No puedes agregar más de 1000 unidades por producto")
    private Integer cantidad;
    
    private Double precioUnitario;  // Solo lectura

    public ProductoCarritoDTO(ProductoCarrito pc) {
        this.id = pc.getId();
        this.productoId = pc.getProducto().getId();
        this.nombreProducto = pc.getProducto().getNombre();
        this.cantidad = pc.getCantidad_producto();
        this.precioUnitario = pc.getProducto().getPrecio();
    }
}
