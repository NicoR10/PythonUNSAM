import random
import matplotlib.pyplot as plt
import numpy as np


def busqueda_secuencial(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición,
    de lo contrario devuelve -1.
    '''
    pos = -1
    for i, z in enumerate(lista):
        if z == x:
            pos = i
            break
    return pos


def busqueda_secuencial_(lista, x):
    '''Devuelve una tupla de dos elementos:
    1) Si x está en la lista devuelve el índice de su primer aparición,
    de lo contrario devuelve -1.
    2) Devuelve adicionalmente la cantidad de comparaciones realizadas.
    '''
    comps = 0  # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i, z in enumerate(lista):
        comps += 1  # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps


def busqueda_binaria(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:                # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    return pos


def busqueda_binaria_(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve una tupla de dos elementos:
    1) Si x está en la lista devuelve el índice de su primer aparición,
    de lo contrario devuelve -1.
    2) Devuelve adicionalmente la cantidad de comparaciones realizadas.
    
    '''
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    comps = 0
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            comps += 1
            break
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
            comps += 1
        else:                # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    return pos, comps


def generar_lista(n, m):
    '''
    Devuelve una lista aleatoria de largo n, con valores entre 0 y m
    '''
    l = random.sample(range(m), k=n)
    l.sort()
    return l


def generar_elemento(m):
    '''
    Genera un entero entre 0 y m-1
    '''
    return random.randint(0, m-1)


def experimento_secuencial_promedio(lista, m, k):
    '''Devuelve la cantidad de comparaciones promedio realizadas por la
    busqueda secuencial para buscar un elemento k veces en la lista.
    '''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista, x)[1]

    comps_prom = comps_tot / k
    return comps_prom


def experimento_binario_promedio(lista, m, k):
    '''Devuelve la cantidad de comparaciones promedio realizadas por la
    busqueda binaria para buscar un elemento k veces en la lista.
    '''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_(lista, x)[1]

    comps_prom = comps_tot / k
    return comps_prom

# %%


m = 10000
n = 100
k = 1000

largos = np.arange(256) + 1  # estos son los largos de listas que voy a usar
comps_promedio = np.zeros(256)  # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
comps_promedio_binaria = np.zeros(256)

for i, n in enumerate(largos):
    lista = generar_lista(n, m)  # genero lista de largo n
    comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)
    comps_promedio_binaria[i] = experimento_binario_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos, comps_promedio, label='Búsqueda Secuencial')
plt.plot(largos, comps_promedio_binaria, label='Búsqueda Binaria')
plt.xlabel("Largo de la lista")
plt.xlim(1, 50)
plt.ylabel("Cantidad de comparaciones")
plt.ylim(1, 50)
plt.title("Complejidad de la Búsqueda")
plt.legend()
