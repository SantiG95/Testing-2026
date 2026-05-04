package com.uade.tpo.e_commerce3.controller;

import java.util.List;

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
import org.springframework.web.bind.annotation.RestController;

import com.uade.tpo.e_commerce3.dto.UsuarioDTO;
import com.uade.tpo.e_commerce3.model.Usuario;
import com.uade.tpo.e_commerce3.service.UsuarioService;

@RestController
@RequestMapping("/api/usuarios")
public class UsuariosController {
    
        @Autowired
        private UsuarioService usuarioService;

         @GetMapping
        public ResponseEntity<List<UsuarioDTO>> getAllUsuarios() {
            List<UsuarioDTO> usuarios = usuarioService.getAllUsuarios();
            return new ResponseEntity<>(usuarios, HttpStatus.OK);
    }

        @GetMapping("/{id}")
        public ResponseEntity<UsuarioDTO> getUsuarioById(@PathVariable Long id) {
            UsuarioDTO usuario = usuarioService.getUsuarioById(id);
            return new ResponseEntity<>(usuario, HttpStatus.OK);
    }

        @DeleteMapping("/{id}")
        public ResponseEntity<Void> deleteUsuarioById(@PathVariable Long id) {
            usuarioService.deleteUsuarioById(id);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }

        @PostMapping
        public Usuario saveUsuario(@RequestBody Usuario usuario) {
            return usuarioService.saveUsuario(usuario);

        }
        
        @PutMapping("/{id}")
        public ResponseEntity<UsuarioDTO> updateUsuario(@PathVariable Long id, @RequestBody UsuarioDTO usuario) {
            UsuarioDTO actualizado = usuarioService.updateUsuario(id, usuario);
            return new ResponseEntity<>(actualizado, HttpStatus.OK);
    }


}
