notas = (10, 61, 0, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100)

promedio = sum(notas) / len(notas)

print("Promedio del estudiante:", promedio)

aprobo = promedio >= 51

print("El estudiante aprobo?: ", aprobo)