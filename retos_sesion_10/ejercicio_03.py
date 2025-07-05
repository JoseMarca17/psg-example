tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

conjunto_tienda_fisica = set(tienda_fisica)
conjunto_tienda_online = set(tienda_online)
print('Personas que compraron en tienda fisica: ', conjunto_tienda_fisica)
print('Personas que compraron de forma online: ', conjunto_tienda_online)

compra_en_ambos = conjunto_tienda_fisica.intersection(conjunto_tienda_online)
print("\nPersonas que compraron en ambos canales: ", compra_en_ambos)

compra_fisica = conjunto_tienda_fisica.difference(conjunto_tienda_online)
print("\nPersonas que compraron solo en tienda fisica: ", compra_fisica)

compra_online = conjunto_tienda_online.difference(conjunto_tienda_fisica)
print("\nPersonas que compraron solo online: ", compra_online)