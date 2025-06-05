# Como usar y declarar cadenas 
simple = 'Mi cadena permite comillas "dobles" en una sola línea'
doble  = "Mi cadena permite comillas 'simples' en una sola línea"
triple_simple = '''Mi cadena
permite contenido 
en varias líneas y comillas "dobles" '''
triple_doble = """Mi cadena
permite contenido 
en varias líneas y comillas 'simples' """
print (simple)
print (doble)
print (triple_simple)
print (triple_doble)

# Convierte otro tipo de datos en mediante el metodo str 

entero = str(1)
flotante = str(1E-3)
hexadecimal = str(0xA)
booleano = str (True)
print (entero)
print (flotante)
print (hexadecimal)
print (booleano)
print (type(entero))
print (type(flotante))
print (type(hexadecimal))
print (type(booleano))

# Escape de caracteres para usar algun tipo de caracter especial 

print ("El mensaje enviado fue: \"Hello, I\'m a message\"")
print ('El mensaje enviado fue: \"Hello, I\'m a message\"')

# Escribir metodos como tabulados o saltos de linea dado por el lenguaje 

mensaje = "Hola,\n\teste es un mensaje \vcon algunos caracteres \
especiales como \\ y tabulador."
print(mensaje)


# Comm introducir datos mediante la terminal para cadenas 

entrada = input("Ingrese un valor: ")
print (entrada)
print (type(entrada))

# Cuando introducimos por teclado y es procesado por una 
# cadena puede ser convertido a diferentes tipos como enteros, flotantes, booleanos

entero = int(input("Ingrese un valor entero: "))
print (entero, type(entero))

flotante = float(input("Ingrese un valor flotante: "))
print (flotante, type(flotante))

booleano = bool(input("Ingrese un valor booleano: "))
print (booleano, type(booleano))

# Manejo e indices dentro de una cadena

print ("Indexado positivo")
fruta = "banana"
print (fruta)
print (fruta[0])
print (fruta[5])

print ("Indexado negativo")
fruta = "banana"
print (fruta)
print (fruta[-1])
print (fruta[-3])

# Usando slicing 

print ("Slicing")
ciudad =  "LaPaz-Bolivia"
print (ciudad)
print ("Slicing con índices positivos")
print (ciudad[0:6])
print (ciudad[0:6:2])
print ("Slicing con índices negativos")
print (ciudad[-10:-2])
print (ciudad[-10:-2:2])

# Dejando el espacio nos dice que se toma todo el texto 

print ("Slicing sin índice inicial y final")
print (ciudad[:6])
print (ciudad[6:])
print ("Slicing sin índice inicial ni final")
print (ciudad[:])
print (ciudad[::2])

# Slicing con paso negativo 

print ("Slicing con paso negativo")
print (ciudad[10:4:-1])
print (ciudad[10::-2])

# Concatenacion de una cadena 

print ("Concatenación de cadenas")
cadena1 = "Hola"
cadena2 = "Mundo"
concatenada = cadena1 + " " + cadena2
print (concatenada)

#Repeticion de cadenas 

print ("Repetición de cadenas")
cadena = "-#-"
repetida = cadena * 10
print (repetida)

# Longitud de cadenas 

print ("Longitud de una cadena")
cadena = "Hola Mundo :D"
longitud = len(cadena)
print (cadena)
print (longitud, type(longitud))

# Metodos con cadenas 

print ("Función Upper")
cadena = "cadena Inicial #1"
mayuscula  = cadena.upper()
print (cadena)
print (mayuscula)

print ("Función Lower")
cadena = "Cadena INICIAL #2"
minuscula  = cadena.lower()
print (cadena)
print (minuscula)

print ("Función Capitalize")
cadena = "cadena INICIAL #3"
capital = cadena.capitalize()
print (cadena)
print (capital)

print ("Función Title")
cadena = "CADENA inicial #4"
titulo = cadena.title()
print (cadena)
print (titulo)

print ("Función Swapcase")
cadena = "CADena InIcIaL #5"
swap = cadena.swapcase()
print (cadena)
print (swap)

print ("Función Count")
cadena = "Cantidad de veces la letra A"
contar = cadena.count("a")
print(cadena)
print(contar, type(contar))

print ("Función Find")
cadena = "Encontrar las letras las"
buscar = cadena.find("las")
print(cadena)
print(buscar, type(buscar))

print ("Función Rfind")
cadena = "Encontrar las letras las"
buscar = cadena.rfind("las")
print(cadena)
print(buscar, type(buscar))

print ("Función Find y Rfind")
cadena = "Encontrar tres O"
buscar = cadena.find("OOO")
print(cadena)
print(buscar, type(buscar))
buscar = cadena.rfind("OOO")
print(buscar, type(buscar))

# Funciones para saber el contenido de caracteres

print ("Función isdigit")
resultado = "100".isdigit()
print (resultado, type(resultado))
print ("Función isalpha")
resultado = "Hola".isalpha()
print (resultado, type(resultado))
print ("Función isalnum")
resultado = "usuario123".isalnum()
print (resultado, type(resultado))

# Separador de cadenas 

print ("Función split")
cadena = "pan,carne,huevos"
separado = cadena.split(",")
print (cadena)
print (separado, type(separado))

# Concatena cadenas 

print ("Función join")
cadena = "abcdefghij"
unido = "-".join(cadena)
print (cadena)
print (unido)

# Remueve los valores a la izquierda print ("Función strip")
cadena = "      Hola    Mundo     "
limpio = cadena.strip()
print (cadena)
print (limpio)
cadena = "-abc--def-ghi-cba----"
limpio = cadena.strip("bac-")
print (cadena)
print (limpio)

# Reemplazo de contenidos 

print ("Función replace")
cadena = "Me gusta programar en JS, Amo JS"
reemplazado = cadena.replace("JS", "Python")
print (cadena)
print (reemplazado)

# Insertar contenido en cadena 

print ("Función format")
cadena = "El valor de PI es: {}"
formateado = cadena.format(3.1416)
print (cadena)
print (formateado)