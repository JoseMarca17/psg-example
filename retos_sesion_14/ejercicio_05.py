def contar_vocales(cadena):
    vocales = ["a","e","i","o", "u"]
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

cadena = input("Ingrese una cadena: ").lower()
vocales = contar_vocales(cadena)
print(f"La cadena '{cadena}' tiene: {vocales} vocales")
