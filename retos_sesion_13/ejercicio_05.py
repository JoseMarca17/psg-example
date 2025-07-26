for fila in range(8):
    for columna in range(8):
        if (columna + fila) % 2 == 0:
            print ("#", end=" ")
        else:
            print("*", end=" ")
    print()
