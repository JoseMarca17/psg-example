def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(fila)
    print()

def verificar_ganador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True
    return False

def verificar_tablero(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

def tres_en_raya():
    tablero = crear_tablero()
    turno = "X"

    while True:
        print(f"\nTurno de '{turno}'")
        mostrar_tablero(tablero)

        fila = int(input("Ingresa fila (0-2): "))
        columna = int(input("Ingresa columna (0-2): "))
        
        if fila < 0 or fila > 2 or columna < 0 or columna > 2:
            print("Posición invalida. Intenta de nuevo.\n")
            continue
        if tablero[fila][columna] != " ":
            print("La casilla ya esta ocupada.\n")
            continue

        tablero[fila][columna] = turno

        if verificar_ganador(tablero):
            mostrar_tablero(tablero)
            print(f"\n¡Jugador '{turno}' ha ganado!")
            break

        if verificar_tablero(tablero):
            mostrar_tablero(tablero)
            print("\n¡Empate!")
            break

        turno = "O" if turno == "X" else "X"

tres_en_raya()
