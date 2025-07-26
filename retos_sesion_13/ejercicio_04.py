while True:
    frase = input("\nEscribe una frase: (o escribe salir par terminar): ").lower()
    if frase == 'salir':
        print("Saliendo del programa ...")
        break

    frase_sin_espacios = ''.join(frase.split())
    if frase_sin_espacios == frase_sin_espacios[::-1]:
        print("\n😊 Es una frase palindroma")
    else:
        print("\n🤖 No es una frase palindroma")
