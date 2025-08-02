def separar_numeros(numeros):
    numeros_pares = []
    numeros_impares = []
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
        else:
            numeros_impares.append(numero)
    return numeros_pares, numeros_impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares, numeros_impares = separar_numeros(numeros)
print(f"La lista original es: {numeros}")
print(f"La lista de numeros pares es: {numeros_pares}")
print(f"La lista de numeros impares es: {numeros_impares}")
