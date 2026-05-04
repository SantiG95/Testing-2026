package com.uade.tpo.e_commerce3.dto;

import com.uade.tpo.e_commerce3.model.Usuario;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class UsuarioDTO {
    private Long id;
    private String username;
    private String mail;
    private String nombre;
    private String apellido;

    public UsuarioDTO(Usuario usuario) {
        this.id = usuario.getId();
        this.username = usuario.getUsername();
        this.mail = usuario.getMail();
        this.nombre = usuario.getNombre();
        this.apellido = usuario.getApellido();
    }
}
