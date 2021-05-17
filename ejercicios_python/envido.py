import random
from collections import Counter


valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor, palo) for valor in valores for palo in palos]


def buscar_envido():
    '''
    Pide una mano y se fija si hay envido.
    Retorna el puntaje.
    Para mas detalle descomentar los prints
    '''
    mano = random.sample(naipes, k=3)
    #print('Mano: ', mano)
    cartas_validas_para_envido = [(valor,palo) for (valor, palo) in mano if valor < 10]
    #print('Cartas que pueden sumar: ', cartas_validas_para_envido)
    palos_de_la_mano = [palo for (valor, palo) in mano if valor < 10]
    palo_repetido = Counter(palos_de_la_mano).most_common(1)
    #print('Palo y repeticiones: ', palo_repetido)
    valores_de_la_mano = [valor for (valor, palo) in cartas_validas_para_envido if palo == palo_repetido[0][0]]
    #print('Numero de los palos repetidos: ', valores_de_la_mano)
    
    if len(cartas_validas_para_envido) < 2:
        #print('No hay envido')
        return 0
    else:
        if palo_repetido[0][1] == 1:
            #print('No hay envido')
            return 0
        elif palo_repetido[0][1] == 2:
            #print('Hay chance de envido')
            puntaje = sum(valores_de_la_mano) + 20
            #print(puntaje)
            return puntaje
        else:
            #print('Hay 3 palos iguales hay que elegir las dos mayores')
            valores_ordenados = valores_de_la_mano.copy()
            valores_ordenados.sort()
            puntaje = valores_ordenados[1] + valores_ordenados[2] + 20
            return puntaje
 
# %% Probabilidad de obtener 31, 32 o 33 puntos en una mano


N = 1000000

resultados = [buscar_envido() for _ in range(N)]

G = sum([1 for resultado in resultados if resultado == 31])
prob = G/N
print(f'Jugué {N} veces, de las cuales {G} saqué envido con 31.')
print(f'Podemos estimar la probabilidad de sacar envido con 31 mediante {prob:.6f}.')

G = sum([1 for resultado in resultados if resultado == 32])
prob = G/N
print(f'Jugué {N} veces, de las cuales {G} saqué envido con 32')
print(f'Podemos estimar la probabilidad de sacar envido con 32 mediante {prob:.6f}.')

G = sum([1 for resultado in resultados if resultado == 33])
prob = G/N
print(f'Jugué {N} veces, de las cuales {G} saqué envido con 33')
print(f'Podemos estimar la probabilidad de sacar envido con 33 mediante {prob:.6f}.')