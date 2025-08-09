class FrutaNoValida(Exception):
    pass

frutas_permitidas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]
canasta = []

while True:
    try:
        print('\n\t','-'*10,"Canasta de frutas",'-'*10)
        print("Frutas permitidas:", " ".join(frutas_permitidas))
        print("Escribe 'salir' para cerrar el programa")
        fruta = input("\nIngrese una fruta: ")

        if fruta.lower() == "salir":
            print("La canasta contiene: ", "".join(canasta))
            print("\nPrograma finalizado.")
            break

        if fruta not in frutas_permitidas:
            raise FrutaNoValida("Solo se permitene las frutas: ", "".join(frutas_permitidas))

        canasta.append(fruta)
        print(f"La fruta: {fruta} fue agregada correctamente a la canasta.")

    except FrutaNoValida as e:
        print(f" Error: {e}")
    except Exception as e:
        print(f" Error inesperado: {e}")
