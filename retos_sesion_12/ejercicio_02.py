usuarios = {
    "admin": "admin123",
    "user1": "user123",
    "user2": "user123",
    "user3": "user123"
}

usuario = input("Ingresa el nombre de usuario: ")
password = input("Ingresa la contraseña: ")

if usuario in usuarios and usuarios[usuario] == password:
    print("Acceso Aprobado")
    print("Accediendo a la app ....")
else:
    print("Acceso Denegado")
