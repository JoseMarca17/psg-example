nombre = input("Nombre: ")
telefono = input("Teléfono: ")

telefono_sin_signo = telefono[1:] if telefono.startswith('+') else telefono
telefono_valido = telefono.startswith('+') and telefono_sin_signo.isdigit() and len(telefono_sin_signo) == 11

if nombre and telefono_valido:
    contactos = []
    contactos.append((nombre, telefono))
    print("-------------")
    print("Contacto guardado")
else:
    print("-------------")
    print("Datos incorrectos")
