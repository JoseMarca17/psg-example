palabra = "Python"
print(palabra.center(10, '-')) 

texto = "Hola\tMundo"
resultado = texto.expandtabs(4)
print("Texto expandido:", resultado)

info = {"animal": "gato"}
frase = "Mi animal favorito es un {animal}."
resultado = frase.format_map(info)
print("Frase formateada:", resultado)

texto1 = "Hola"
texto2 = "¡Hola!"
texto3 = "Café"

print(texto1.isascii())  
print(texto2.isascii())  
print(texto3.isascii())  


frase = "nombre: Juan"
resultado = frase.partition(":")
print(resultado)  
palabra = "correo@example.com"
usuario, arroba, dominio = palabra.partition("@")
print("Usuario:", usuario)
print("Dominio:", dominio)
