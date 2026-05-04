package com.uade.tpo.e_commerce3.service;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import com.uade.tpo.e_commerce3.dto.ProductoDTO;
import com.uade.tpo.e_commerce3.dto.ProductoEliminadoDTO;
import com.uade.tpo.e_commerce3.exception.ProductoNotFoundException;
import com.uade.tpo.e_commerce3.model.Categoria;
import com.uade.tpo.e_commerce3.model.Producto;
import com.uade.tpo.e_commerce3.repository.CategoriaRepository;
import com.uade.tpo.e_commerce3.repository.ProductoRepository;

import jakarta.transaction.Transactional;

@Service //se encarga de las operaciones del negocio, si sale error cancela todo.
@Transactional
public class ProductoService {
 
    @Autowired
    private ProductoRepository productoRepository;
    
    @Autowired
    private CategoriaRepository categoriaRepository;
    
    public List<ProductoDTO> getAllProductos() {
        List<Producto> productos = productoRepository.findAll(Sort.by(Sort.Direction.ASC, "nombre"));
        return productos.stream()
                .map(producto -> new ProductoDTO(
                    producto.getId(),
                    producto.getNombre(),
                    producto.getDescripcion(),
                    producto.getPrecio(),
                    producto.getStock(),
                    producto.getFoto(),
                    producto.getCategorias().stream().map(Categoria::getNombre).collect(Collectors.toList())
                ))
                .collect(Collectors.toList());           
    }

    public List<Categoria> getAllCategorias() {
        return categoriaRepository.findAll();
    }

    public ProductoDTO getProductoById(Long id) {
        Producto producto = productoRepository.findById(id).orElse(null);
        if (producto == null) {
            throw new ProductoNotFoundException("Producto no encontrado con id: " + id );
        }
        ProductoDTO productoDTO = new ProductoDTO(producto.getId(), producto.getNombre(), producto.getDescripcion(), producto.getPrecio(), producto.getStock(), producto.getFoto(), producto.getCategorias().stream().map(Categoria::getNombre).collect(Collectors.toList()));
        return productoDTO;
    }

    public ProductoEliminadoDTO deleteProductoById(Long id) {
        Producto producto = productoRepository.findById(id)
            .orElseThrow(() -> new ProductoNotFoundException("Producto no encontrado con id: " + id));
        String nombre = producto.getNombre();
        productoRepository.deleteById(id);
        return new ProductoEliminadoDTO(id, nombre);
    }

    public ProductoDTO saveProducto(ProductoDTO productoDTO) {
        Producto producto = new Producto();
        producto.setNombre(productoDTO.getNombre());
        producto.setDescripcion(productoDTO.getDescripcion());
        producto.setPrecio(productoDTO.getPrecio());
        producto.setStock(productoDTO.getStock());
        producto.setFoto(productoDTO.getFoto());
        
        // Buscar categorías existentes y crear las que no existan
        List<Categoria> categoriasEntity = new ArrayList<>();
        if (productoDTO.getCategorias() != null) {
            for (String nombreCategoria : productoDTO.getCategorias()) {
                List<Categoria> existente = categoriaRepository.findByNombreIn(List.of(nombreCategoria));
                if (existente.isEmpty()) {
                    Categoria nuevaCategoria = new Categoria();
                    nuevaCategoria.setNombre(nombreCategoria);
                    categoriaRepository.save(nuevaCategoria);
                    categoriasEntity.add(nuevaCategoria);
                } else {
                    categoriasEntity.add(existente.get(0));
                }
            }
        }
        producto.setCategorias(categoriasEntity);



        Producto productoGuardado = productoRepository.save(producto);
        
        return new ProductoDTO(
            productoGuardado.getId(), 
            productoGuardado.getNombre(), 
            productoGuardado.getDescripcion(), 
            productoGuardado.getPrecio(),
            productoGuardado.getStock(),
            productoGuardado.getFoto(),
            productoGuardado.getCategorias().stream().map(Categoria::getNombre).collect(Collectors.toList())
        );
    }

   /*  public ProductoDTO updateProducto(Long id, ProductoDTO producto) {
        ProductoDTO existingProducto = getProductoById(id);
        if (existingProducto != null) {
            existingProducto.setNombre(producto.getNombre());
            existingProducto.setDescripcion(producto.getDescripcion());
            existingProducto.setPrecio(producto.getPrecio());
            return productoRepository.save(existingProducto);
        }
        return null;
    }*/


    public ProductoDTO updateProducto(Long id, ProductoDTO producto) {
    // 1. Buscamos la ENTIDAD, no el DTO (usamos findById directamente)
    Producto existingProducto = productoRepository.findById(id)
            .orElseThrow(() -> new ProductoNotFoundException("Producto no encontrado con id: " + id));
    // 2. Mapeamos los cambios del DTO a la ENTIDAD
    existingProducto.setNombre(producto.getNombre());
    existingProducto.setDescripcion(producto.getDescripcion());
    existingProducto.setPrecio(producto.getPrecio());
    // 3. Guardamos la ENTIDAD y la convertimos a DTO para devolverla
    Producto productoGuardado = productoRepository.save(existingProducto);
    return new ProductoDTO(
            productoGuardado.getId(), 
            productoGuardado.getNombre(), 
            productoGuardado.getDescripcion(), 
            productoGuardado.getPrecio(),
            productoGuardado.getStock(),
            productoGuardado.getFoto(),
            productoGuardado.getCategorias().stream().map(Categoria::getNombre).collect(Collectors.toList())
        );
    }

    public ProductoDTO updateStock(Long id, int cantidad) {
        Producto producto = productoRepository.findById(id)
                .orElseThrow(() -> new ProductoNotFoundException("Producto no encontrado con id: " + id));
        producto.setStock(cantidad);
        productoRepository.save(producto);

        return new ProductoDTO(
            producto.getId(), 
            producto.getNombre(), 
            producto.getDescripcion(), 
            producto.getPrecio(),
            producto.getStock(),
            producto.getFoto(),
            producto.getCategorias().stream().map(Categoria::getNombre).collect(Collectors.toList())
        );
    }
}
