class FondosInsuficientesError(Exception):
    pass

saldo_disponible = 1200 

print('\n\t','-'*10,"CAJERO AUTOMATICO",'-'*10)
print(f"Saldo disponible: {saldo_disponible} Bs")

try:
    monto = float(input("Ingrese el monto a retirar: "))
    
    if monto <= 0:
        raise Exception("Monto invalido. El monto a retirar debe ser mayor a cero")

    if monto > 1000:
        raise Exception("Monto excede el límite de 1000 Bs por transacción.")

    if monto > saldo_disponible:
        raise FondosInsuficientesError(
        f"Fondos insuficientes. Intentaste retirar {monto}, pero solo tienes {saldo_disponible}.")

    saldo_disponible -= monto
    print(f" Retiro exitoso. Saldo restante: {saldo_disponible} Bs")

except FondosInsuficientesError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Debe ingresar un valor numérico válido.")
except Exception as e:
    print(f"Error: {e}")
