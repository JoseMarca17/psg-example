def calcular_promedio(calificaciones):
    promedio = sum(calificaciones)/len(calificaciones)
    return promedio


calificaciones = [50, 75, 80, 91, 70]
promedio = calcular_promedio(calificaciones)
print(f"El promedio de las calidicaciones {calificaciones} es : {promedio}")