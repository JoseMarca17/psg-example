arca = {"🐶" : 2, "🐱" : 2, "🐯" : 2, "🐵" : 2, "🦄" : 0, "🦒" : 1}
print("Animales dentro del arca ")
print(arca)

arca.update({"🐿️": 2,  "🐎": 2,  "🐔": 2 })
print("\nAnimales añadidos al arca: ")
print(arca)

existe = "🐲" in arca
print("\n¿Está el dragón 🐲 en el arca?", existe)

arca.pop("🦄")
arca["🦒"] = 2
print("\nArca actualizada: ")
print(arca)

arca.clear()
print("\nArca despes del diluvio: ")
print(arca)