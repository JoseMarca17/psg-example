habitats_en_peligro = {
    "polo norte": {
        "especies": {"oso polar", "morsa", "ballena"}
    },
    "amazonas": {
        "especies": {"tigre", "mono", "guacamayo"}
    }
}

print("Habitats en peligro de extinxion: ")
print(habitats_en_peligro)

habitats_en_peligro.update({
    "Altiplano andino": {
        "especies": {"condor andino", "vicuña"}
    },
    "Islas Galapagos": {
        "especies": {"tortuga gigante", "iguana marina"}
    }
})

print("\nDiccionario de habitats en peligro actualizada: ")
print(habitats_en_peligro)

existe = "amazonas" in habitats_en_peligro
print("\n¿Existe el hábitat 'amazonas'?: ", existe)

habitats_en_peligro["amazonas"]["especies"].add("anaconda")
print("\nDiccionario actualizado de hábitats en peligro:")
print(habitats_en_peligro)