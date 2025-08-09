while True:
    try:
        print('\n\t','-'*10,"Calculadora",'-'*10)
        print("Escribe 'salir' para cerrar el programa")
        print("\nSeleccione la operacion:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        opcion = input("Ingrese el número de la operacion: ")

        if opcion.lower() == "salir":
            print("Cerrando el programa ...")
            break

        if opcion not in ["1", "2", "3", "4"]:
            raise ValueError("Opción inválida. Debe seleccionar: 1, 2, 3 o 4.")

        num_1 = input("Ingrese el primer numero: ")
        if num_1.lower() == "salir":
            print("Cerrando el programa ...")
            break
        num_1 = float(num_1)

        num_2 = input("Ingrese el segundo numero: ")
        if num_2.lower() == "salir":
            print("Cerrando el programa ...")
            break
        num_2 = float(num_2)

        if opcion == "1":
            suma = num_1 + num_2
            print(f"Resultado: {num_1} + {num_2} = {suma}")
        elif opcion == "2":
            resta = num_1 - num_2
            print(f"Resultado: {num_1} - {num_2} = {resta}")
        elif opcion == "3":
            multiplicacion = num_1 * num_2
            print(f"Resultado: {num_1} * {num_2} = {multiplicacion}")
        elif opcion == "4":
            try:
                division = num_1 / num_2
                print(f"Resultado: {num_1} / {num_2} = {division}")
            except ZeroDivisionError:
                print("\nError: No se puede dividir entre cero.")

    except ValueError as ve:
        print(f"\nError: {ve}")
    except ZeroDivisionError:
        print("\nError: No se puede dividir entre cero.")
    except Exception as e:
        print(f"\nError: {e}")
