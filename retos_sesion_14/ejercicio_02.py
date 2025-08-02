def calcular(num1, num2, operador): 
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        return num1 / num2
    else:
        return "Operación invalida"

entrada = input("Ingresa los numeros y la operacion por comas (Ej: 10,5,+): ")
partes = entrada.split(",")

num1 = float(partes[0])
num2 = float(partes[1])
operador = partes[2].strip()  
resultado = calcular(num1, num2, operador)
print(f"El resultado de {num1} {operador} {num2} es: {resultado}")
