package com.uade.tpo.e_commerce3.model;
import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "Clientes")
public class Cliente {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
}
