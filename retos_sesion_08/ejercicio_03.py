pregunta = input("Ingresa una pregunta (sin signos): ")
tupla_pregunta = (pregunta,)  

tupla_concatenada = ('¿',) + tupla_pregunta + ('?',)

print("Pregunta con signos:", tupla_concatenada)

tupla_repetida = tupla_concatenada * 2

print("Tupla repetida dos veces:", tupla_repetida)
