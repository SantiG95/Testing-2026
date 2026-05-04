package com.uade.tpo.e_commerce3.dto;

import jakarta.validation.constraints.DecimalMin;
import jakarta.validation.constraints.Digits;
import jakarta.validation.constraints.Min;
import lombok.Data;

@Data
public class ProductoUpdateDTO {
    
    @DecimalMin(value = "0.01", message = "El precio debe ser mayor a 0")
    @Digits(integer = 10, fraction = 2, message = "El precio debe tener máximo 10 dígitos y 2 decimales")
    private Double precio;
    
    @Min(value = 0, message = "El stock no puede ser negativo")
    private Integer stock;
}
