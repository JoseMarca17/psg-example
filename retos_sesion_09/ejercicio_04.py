productos = ["Oreo", "Bon Bon Bum","Nucita" , "Chizitos", "Sapito", "Cremositas"]
precios = [2.5, 1.0, 1.5, 2.0, 3.0, 3.5]
print('Lista de productos: ', productos)
print('lista de precios: ', precios)

# Añadir productos
productos.extend(["Groso", "Filipitos"])
precios.extend([0.5, 4.0])
print('\nLista con los 2 productos incluidos: ', productos)
print('lista de precios con los productos incluidos: ', precios)

# ELiminar productos
producto_a_eliminar = 'Bon Bon Bum'
indice = productos.index(producto_a_eliminar)
productos.pop(indice)
precios.pop(indice)
print(f"\nIndice en el que se encuentra el producto {producto_a_eliminar} : {indice}")
print(f'Producto y precio con el indice {indice} eliminado')
print('Lista actualizada de productos: ', productos)
print('Lista actualizada de precios: ', precios)

# Buscar precios 
precio_oreo = precios[productos.index("Oreo")]
print('\nEl precio del oreo es:', precio_oreo)
precio_chizitos = precios[productos.index("Chizitos")] 
print('El precio de los Chizitos es:', precio_chizitos)

# Producto mas caro y mas barato
precio_max = max(precios)
precio_min = min(precios)
producto_caro = productos[precios.index(precio_max)]
producto_barato = productos[precios.index(precio_min)]
print('\nEl producto mas caro es:', producto_caro)
print('El producto mas caro es:', producto_barato)

# Cantidad de productos
total_cantidad = len(productos)
print('\nLa cantidad total de productos es: ', total_cantidad)

# Suma de todos los productos
total_costos = sum(precios)
print('\nLa suma del costo de todos los productos es:', total_costos)

'''Ordenamos mediante el uso de listas por comprension
Se genera una lista de indices con los precios ordenados
Se tomo la lista en base al rango de el tamaño de la lista para que va de 0 hasta len()-1
Se uso el metodo __getitem__ para obtener los valores de los precios como lo explica en el libro
python para todos de la bibliografia que esta en el repositorio y se ordena con el sorted en base 
a esos valores
'''

indices_precios_ordenados = sorted(range(len(precios)), key=precios.__getitem__) 
productos = [productos[i] for i in indices_precios_ordenados] 
precios = [precios[i] for i in indices_precios_ordenados] 
print("\nProductos ordenados del más barato al más caro:", productos) 
print("Precios ordenados del más barato al más caro:", precios)

#Eliminar todos los productos y precios
productos.clear()
precios.clear()

print('\nLista con los productos eliminados: ', productos)
print('Lista con los precios eliminados: ', precios)