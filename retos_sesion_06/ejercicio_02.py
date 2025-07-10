print("|   A   |   B   |  XNOR |")
print("-"*25)
a = False
b = False
resultado = (a and b) or (not a and not b)
print(f"| {a} | {b} | {resultado}  |")

a = False
b = True
resultado = (a and b) or (not a and not b)
print(f"| {a} | {b}  | {resultado} |")

a = True
b = False
resultado = (a and b) or (not a and not b)
print(f"| {a}  | {b} | {resultado} |")

a = True
b = True
resultado = (a and b) or (not a and not b)
print(f"| {a}  | {b}  | {resultado}  |")
