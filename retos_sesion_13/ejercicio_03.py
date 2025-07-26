estudiantes = [('Miguel', 51), ('Daniel', 80), ('Virginia', 90), ('Franco', 40), ('Flabio', 30)]

for nombre, nota in estudiantes: 
    if nota >= 51:
        print(f"Felicitaciones estudiante: {nombre} por haber aprobado con una nota de {nota}")