tupla_animales = (('canino', '🐶'), ('felino', '🐱'), ('aves', ['🐦', '🦅']))
animales = dict(tupla_animales)
print("Diccionario inicial:", animales)


valor_eliminado = animales.pop('aves')
print("Valor obtenido:", valor_eliminado)
print("Diccionario actualizado: ")
print(animales)

animales['felino'] = '🐈'
print("Diccionario modificado: ", animales)

# Cambiar clave 'canino' por 'caninos'
animales['caninos'] = animales.pop('canino')
animales['caninos'] = ['🐶', '🐕']
print("Diccionario final:", animales)
