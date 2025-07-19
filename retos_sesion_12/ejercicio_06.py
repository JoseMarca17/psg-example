# Solicitar operación
entrada = input("Ingrese la operación en el formato número1, número2, operación : ")

valores = entrada.split(',')

if len(valores) == 3:
    num1_str = valores[0].strip()
    num2_str = valores[1].strip()
    operacion = valores[2].strip()
    
    num1 = float(num1_str)
    num2 = float(num2_str)
    if operacion == '+':
        resultado = num1 + num2
        print(f"{num1} {operacion} {num2}")
        print("Resultado:", resultado)
    elif operacion == '-':
        resultado = num1 - num2
        print(f"{num1} {operacion} {num2}")
        print("Resultado:", resultado)
    elif operacion == '*':
        resultado = num1 * num2
        print(f"{num1} {operacion} {num2}")
        print("Resultado:", resultado)
    elif operacion == '/':
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} {operacion} {num2}")
            print("Resultado:", resultado)
        else:
                print("Error: División por cero.")
    else:
            print("Operación inválida. Usa +, -, * o /.")
else:
    print("Formato incorrecto. Utiliza el formato: número1, número2, operación")
