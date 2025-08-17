cont = 0
num = 1
print("Primeros 20 números múltiplos de 2 y de 5:")

while cont < 20:
    if num % 2 == 0 and num % 5 == 0:
        print(num, end="  ")
        cont += 1
    num += 1

print()
