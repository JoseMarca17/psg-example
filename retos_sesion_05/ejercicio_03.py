tiempo = 1000000
tiempo_inicial = tiempo
semana = 7*24*60*60  
dia = 24*60*60
hora = 60*60
minuto = 60
tiempo_semana = tiempo//semana
tiempo = tiempo - semana * tiempo_semana
tiempo_dia = tiempo//dia
tiempo = tiempo - dia * tiempo_dia
tiempo_hora = tiempo//hora
tiempo = tiempo - hora * tiempo_hora
tiempo_minuto = tiempo//minuto
tiempo = tiempo - minuto * tiempo_minuto
print("🕐 ",tiempo_inicial, " segundo es igual a ", tiempo_semana, " semanas", tiempo_dia, 
    " dias", tiempo_hora, " horas", tiempo_minuto, " minutos y ", tiempo, " segundos")   