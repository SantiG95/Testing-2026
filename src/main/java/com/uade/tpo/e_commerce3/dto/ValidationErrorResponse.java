package com.uade.tpo.e_commerce3.dto;

import java.util.HashMap;
import java.util.Map;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class ValidationErrorResponse {
    private String mensaje;
    @Builder.Default
    private Map<String, String> errores = new HashMap<>();
    private int codigo;
}
