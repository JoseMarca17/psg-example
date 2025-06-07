cadena = input("Ingrese una cadena palindrome: ").lower().replace(" ", "")
print(cadena)
cadena_invertida = cadena[-1::-1]
print(cadena_invertida)
es_palindrome = cadena == cadena_invertida
print(f"La cadena {cadena} es palindrome? : {es_palindrome}")