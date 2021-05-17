from collections import Counter
import csv
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

def leer_parque(nombre_de_archivo, parque):
    arboles = []
    with open(nombre_de_archivo, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for line in reader:
            arbol = dict(zip(headers, line))
            if arbol['espacio_ve'] == parque:
                arboles.append(arbol)
    return arboles


def especies(lista_arboles):
    especies = set()
    for arbol in lista_arboles:
        especies.add(arbol['nombre_com'])
    return especies


def contar_ejemplares(lista_arboles):
    tenencias = Counter()
    for arbol in lista_arboles:
        tenencias[arbol['nombre_com']] += 1
    return tenencias


def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas.append(float(arbol['altura_tot']))
    return alturas


def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(float(arbol['inclinacio']))
    return inclinaciones


def especimen_mas_inclinado(lista_arboles):
    especie = ''
    inclinacion_max = 0.0
    especie_inclinacion = [especie, inclinacion_max]
    for arbol in lista_arboles:
        inclinacion = float(arbol['inclinacio'])
        if inclinacion >= inclinacion_max:
            inclinacion_max = inclinacion
            especie = arbol['nombre_com']
            especie_inclinacion[0] = especie
            especie_inclinacion[1] = inclinacion
    return especie_inclinacion


def especie_promedio_mas_inclinada(lista_arboles):
    inclinaciones_por_especie = Counter()
    especies_actuales = especies(lista_arboles)
    cantidad_por_especie = contar_ejemplares(lista_arboles)
    especie_inclincacion_prom = {}
    max = 0
    for arbol in lista_arboles:
        inclinaciones_por_especie[arbol['nombre_com']] += float(arbol['inclinacio'])
    for especie in especies_actuales:
        inclinacion_prom = inclinaciones_por_especie[especie]/cantidad_por_especie[especie]
        especie_inclincacion_prom[especie] = inclinacion_prom
        if inclinacion_prom >= max:
            max = inclinacion_prom
            especie_maxima = especie
    return [especie_maxima, max]


def leer_arboles(nombre_de_archivo):
    arboleda = []
    with open(nombre_de_archivo, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for line in reader:
            arbol = dict(zip(headers, line))
            arboleda.append(arbol)
    return arboleda


parque_general_paz = leer_parque('Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
parque_los_andes = leer_parque('Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
parque_centenario = leer_parque('Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

especies_general_paz = especies(parque_general_paz)
especies_los_andes = especies(parque_los_andes)
especies_centenario = especies(parque_centenario)

contar_ejemplares_general_paz = contar_ejemplares(parque_general_paz)
contar_ejemplares_los_andes = contar_ejemplares(parque_los_andes)
contar_ejemplares_centenario = contar_ejemplares(parque_centenario)

print('GENERAL PAZ: ')
pprint(contar_ejemplares_general_paz.most_common(5))
print('LOS ANDES: ')
pprint(contar_ejemplares_los_andes.most_common(5))
print('CENTENARIO: ')
pprint(contar_ejemplares_centenario.most_common(5))

alturas_general_paz = obtener_alturas(parque_general_paz, 'Jacarandá')
alturas_los_andes = obtener_alturas(parque_los_andes, 'Jacarandá')
alturas_centenario = obtener_alturas(parque_centenario, 'Jacarandá')

print('GENERAL PAZ: ')
print('Altura máx: ', max(alturas_general_paz))
print('Altura promedio: ', sum(alturas_general_paz)/len(alturas_general_paz))
print('LOS ANDES: ')
print('Altura máx: ', max(alturas_los_andes))
print('Altura promedio: ', sum(alturas_los_andes)/len(alturas_los_andes))
print('CENTENARIO: ')
print('Altura máx: ', max(alturas_centenario))
print('Altura promedio: ', sum(alturas_centenario)/len(alturas_centenario))

print('CENTENARIO: ')
print(especimen_mas_inclinado(parque_centenario))

print('LOS ANDES: ')
promedio_inclinacion = especie_promedio_mas_inclinada(parque_los_andes)
print(promedio_inclinacion)

# %% 3.18 - 3.19 - 3.20

arboleda = leer_arboles('Data/arbolado-en-espacios-verdes.csv')

H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

HyD = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']


# %% 3.21

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']


def medidas_de_especies(especies, arboleda):
    return {especie: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}


medidas_por_especie = medidas_de_especies(especies, arboleda)

# %% 4.30 - 4.31

plt.figure('Histograma de altos de Jacarandá')
plt.xlim(0, 30)
plt.hist(H, bins=40, color='purple')

altos = [altura for (altura, diametro) in HyD]
diametros = [diametro for (altura, diametro) in HyD]

plt.figure()
plt.scatter(diametros, altos, alpha=0.5, color='green')
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")
