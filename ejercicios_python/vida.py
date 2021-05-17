import datetime

fecha_de_nacimiento = datetime.datetime(1991, 12, 12, 0, 0, 0, 0)
ahora = datetime.datetime.now()
vida = ahora - fecha_de_nacimiento
print('Ahora: ', ahora)
print('Fecha de Nacimiento: ', fecha_de_nacimiento)
print('Mi vida: ', vida)
print('Segundos de vida =', vida.total_seconds())
print('Edad: ', round(vida.days / 365, 1))
