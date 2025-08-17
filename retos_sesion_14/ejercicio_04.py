valor_absoluto = lambda x: x if x >= 0 else -x

numero = float(input("Ingrese el número del cual quiere el valor absoluto: "))
resultado = valor_absoluto(numero)

if resultado == int(resultado):
    resultado = int(resultado)

print(resultado)
