# Conjuntos de autos de cada coleccionista
autos_jhon = {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
autos_jess = {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}

autos_comunes = autos_jhon & autos_jess  

if autos_comunes:
    print("Cantidad de autos en comun:", len(autos_comunes))
    print("Autos en comun:", autos_comunes)
else:
    print("No tienen autos en comun.")
