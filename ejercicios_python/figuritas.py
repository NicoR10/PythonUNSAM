import random
import numpy as np


def crear_album(figus_total):
    return np.zeros(figus_total)


def album_incompleto(album):
    return 0 in album


def comprar_figu(figus_total):
    return random.randint(1, figus_total)


def cuantas_figus(figus_total=670):
    album = crear_album(figus_total)
    figus_compradas = 0
    while album_incompleto(album):
        figurita = comprar_figu(figus_total)
        album[figurita-1] += 1
        figus_compradas += 1
    return figus_compradas

# %% Resultados


figus_total = 6
N = 1000
resultados_para_6 = [cuantas_figus(figus_total) for _ in range(N)]

M = 100
resultados_para_670 = [cuantas_figus() for _ in range(M)]
    
print(f'''Se necesitan en promedio {np.mean(resultados_para_6)} figuritas
para llenar un álbum de 6 figuritas.''')

print(f'''Se necesitan en promedio {np.mean(resultados_para_670)} figuritas
para llenar un álbum de 670 figuritas.''')