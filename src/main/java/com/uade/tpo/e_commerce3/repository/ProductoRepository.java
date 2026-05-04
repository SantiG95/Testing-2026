package com.uade.tpo.e_commerce3.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.uade.tpo.e_commerce3.model.Producto;


//minimiza el boiler plate.
public interface ProductoRepository extends JpaRepository<Producto, Long> {
    //findAll() ya está implementado por JpaRepository, no es necesario definirlo aquí
    // select * from productos

    //save, delete, findById, findAll, update etc. también están implementados por JpaRepository

    //query methods personalizados pueden ser definidos aquí, por ejemplo:
    //findByNombre(String nombre); 
    //findByPrecioBetween(Double minPrecio, Double maxPrecio);
}
