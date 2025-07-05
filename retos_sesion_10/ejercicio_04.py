# Postres pedidos por cada uno
jane = {"Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"}
jhon = {"Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"}

postres_en_comun= jane.intersection(jhon)

total_postres = jane.union(jhon)
 
porcentaje_compatibilidad = (len(postres_en_comun) / len(total_postres)) * 100

print("Postres en común:", postres_en_comun)
print("\nCompatibilidad:", porcentaje_compatibilidad)
print('Deberian replantear su relacion: ', porcentaje_compatibilidad < 50)

