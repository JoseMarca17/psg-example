while True: 
    num = int(input("\nIngrese un numero (o ingrese un 0 para salir): "))
    if num == 0:
        print("Saliendo del programa ...")
        break
    
    if num % 7 == 0:
        print(f"\n😊 El numero {num} es multiplo de 7 ")
    else:
        print(f"\n🤖 El numero {num} no es multiplo de 7 ")
        