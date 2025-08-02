def serie_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return serie_lucas(n - 1) + serie_lucas(n - 2)
 
n_valor = int(input("Ingresa el valor de n-esimo de la serie a ver: "))
print(f"El número {n_valor} de la serie de Lucas es: {serie_lucas(n_valor)}")
