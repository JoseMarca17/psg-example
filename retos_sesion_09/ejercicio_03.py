nombres = ['Pedro', 'Andrea', 'Jose', 'Rafael', 'Paola', 'Daniela', 'Kevin', 'Alejandro'
        , 'Vanesa', 'Jesus']

print("La lista original es: ", nombres)
sublista = nombres[5:9:2]
print('\nLa sublista es: ', sublista)
sublista.sort()
nombre_a_buscar = 'Jose'
print(f"\nNombre a buscar: {nombre_a_buscar}")
print("Existe el nombre en la lista?: ", nombre_a_buscar in nombres)
print('Posicion en la que fue encontrada:', nombres.index(nombre_a_buscar))
print("\nSub lista ordena de A - Z:", sublista)
nombres.sort(reverse=True)
print("\nLista ordenada de Z - A: ", nombres)