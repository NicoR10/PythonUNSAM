# Ejercicios de errores en el código
# %%
# Ejercicio 3.1. Función tiene_a()
'''Comentario:
El error era del tipo semántico ya que no funcionaba bien para
todos los casos de prueba.
Estaba ubicado en la condición else del if y también en la sección anterior al
llegar al while.
Lo corregí sacando el else de la condición y agregando una línea extra para
pasar la expresion de entrada a minuscula y que funcione para expresiones en
mayúscula.
A continuación va el código corregido: '''


def tiene_a(expresion):
    n = len(expresion)
    i = 0
    expresion = expresion.lower()
    while i < n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False


print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))
# %%
# Ejercicio 3.2. Función tiene_a()
'''Comentario:
El error era del tipo sintáctico
Estaba ubicado en la definicion de la función, en el while y en el if.
Faltaba ":"
También pretendía usar "Falso" como booleano cuando lo correcto es false.
Lo corregí agregando los ":" y cambiando Falso por False
A continuación va el código corregido: '''


def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False


print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))
# %%
# Ejercicio 3.3. Función tiene_uno()
'''Comentario:
El error era del tipo semántico
Estaba ubicado en la primer línea, faltaba convertir el parametro expresion a
string.
Lo corregí agregando la línea 63
A continuación va el código corregido: '''


def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i < n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))
# %%
# Ejercicio 3.4. Función suma()
'''Comentario:
El error era del tipo semántico
Estaba ubicado en la linea 87, faltaba el return
Lo corregí agregandole el return
A continuación va el código corregido: '''


def suma(a, b):
    return a + b


a = 2
b = 3
c = suma(a, b)
print(f"La suma da {a} + {b} = {c}")
# %%
# Ejercicio 3.5. Función leer_camion()
'''Comentario:
El error era del tipo semántico.
Estaba ubicado en la parte en que asigna los valores para cada encabezado, se
sobreescribian continuamente los valores y cambia la referencia alojada en
camion.
Lo corregí redefiniendo la estructura de diccionario cada vez que itera sobre
una nueva linea, aunque no es la solución mas optima.
A continuación va el código corregido: '''


import csv
from pprint import pprint


def leer_camion(nombre_archivo):
    camion = []
    registro = {}
    with open(nombre_archivo, "rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = dict()
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion


camion = leer_camion("Data/camion.csv")
pprint(camion)
