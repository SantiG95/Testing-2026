package com.uade.tpo.e_commerce3.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor

//La respuesta del backend al pedido, basicamente lo que hacen los endpoints.
public class ProductoResponse {
    private String nombre;
    private String descripcion;
    private Double precio;
    private Double stock;
}