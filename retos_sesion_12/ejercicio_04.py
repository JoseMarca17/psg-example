edad = int(input("Ingrese la edad: "))
monto_compra = float(input("Ingrese el monto de compra: "))

if edad > 60 and monto_compra > 1000:
    descuento = 0.2
elif 18 <= edad <= 60 and monto_compra > 500:
    descuento = 0.1
else:
    descuento = 0.02

monto_descuento = monto_compra * descuento
total_pagar = monto_compra - monto_descuento

print(f"Descuento aplicado: {descuento * 100}%")
print("Monto descontado: ", monto_descuento)
print("Total a pagar: ", total_pagar)
