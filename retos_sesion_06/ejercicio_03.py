print('''
    Un sistema de seguridad controla el acceso a una habitación, 
    la puerta sólo se abre si se introduce una tarjeta válida o la huella dactilar, 
    pero no ambas al mismo tiempo. 
    Si se introduce la tarjeta y la huella dactilar, la puerta no se abre
    
    ''')
print("OPERADOR XOR")
print("Tarjeta | Huella | Puerta Abierta")
print("-------------------------------")
tarjeta = False
huella = False
puerta = (tarjeta and not huella) or (not tarjeta and huella)
print(tarjeta, "\t", huella, "\t", puerta)

tarjeta = False
huella = True
puerta = (tarjeta and not huella) or (not tarjeta and huella)
print(tarjeta, "\t", huella, "\t", puerta)

tarjeta = True
huella = False
puerta = (tarjeta and not huella) or (not tarjeta and huella)
print(tarjeta, "\t", huella, "\t", puerta)

tarjeta = True
huella = True
puerta = (tarjeta and not huella) or (not tarjeta and huella)
print(tarjeta, "\t", huella, "\t", puerta)
