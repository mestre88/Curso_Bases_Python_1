segundos = input ("digite os segundos que deseja converter em horas: ")
segundostotal = int(segundos)

horas = segundostotal // 3600
segundosrestantes = segundostotal % 3600
minutos = segundosrestantes // 60
segundosrestantesfinal = segundosrestantes % 60

print (horas, "horas, ", minutos, "minutos", segundosrestantesfinal, "segundos")