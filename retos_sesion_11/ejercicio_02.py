alimentos_animales = {
    "carne" : ["gato", 'perro'],
    "pescado": ["gato"],
    "zanahoria" : ["conejo","tortuga"],
    "maiz" : ["gallina"],
    "platano" :["mono", "loro"]
}

print("El diccionario original es:")
print(alimentos_animales)

alimentos_animales.update(
    manzana = ["mono", "loro"],
    alfalfa = ["vaca", "caballo", "conejo"],
    alimento_balanceado = ["perro", "gato"],
    sandia = ["mono", "tortuga", "conejo"]
)

print("\nDicccionario con alimentos añadidos:")
print(alimentos_animales)

existe = "trigo" in alimentos_animales
print("\n¿Existe 'trigo' en el diccionario?: ", existe)

alimentos_animales.pop("zanahoria")
print("\nDiccionario con el alaimento zanahoria eliminado:")
print(alimentos_animales)