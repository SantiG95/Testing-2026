package com.uade.tpo.e_commerce3.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

import com.uade.tpo.e_commerce3.model.Usuario;


public interface UsuarioRepository extends JpaRepository<Usuario, Long> {
    
    Optional<Usuario> findByMail(String mail);
    
    // lo utiliza Spring Security para verificar si el email ya existe antes de registrar un nuevo usuario
    //automaticamente crea la consulta sql: SELECT * FROM usuario WHERE email = ? -> true o false   
    Boolean existsByMail(String mail);
}
