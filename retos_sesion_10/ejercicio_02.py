ropa_deportiva = ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
ropa_formal = ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]

conjunto_ropa_deportiva = set(ropa_deportiva)
conjunto_ropa_formal = set(ropa_formal)

conjunto_prendas = conjunto_ropa_deportiva.union(conjunto_ropa_formal)

print("Prendas para la nueva tienda:", conjunto_prendas)
