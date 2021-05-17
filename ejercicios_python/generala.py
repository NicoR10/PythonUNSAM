import random
from collections import Counter


def tirar(cantidad_de_dados):
    return [random.randint(1, 6) for _ in range(cantidad_de_dados)]


def es_generala(tirada):
    if len(set(tirada)) == 1 and len(tirada) == 5:
        return True
    return False


def contar_repeticiones(tirada):
    tirada_set = set(tirada)
    if len(tirada_set) == 5:
        return [(tirada[0], 1)]
    else:
        cuenta = Counter(tirada).most_common(1)
        return tuple(cuenta)


# %%

def jugar_generala():
    '''Función que juega a la generala, para más detalle y con N chicos,
    descomentar los prints'''
    #print('Tirada ', 1)
    tirada = tirar(5)
    repeticiones = contar_repeticiones(tirada)
    dados_por_tirar = 5 - repeticiones[0][1]
    numero_buscado = repeticiones[0][0]
    #print(tirada)
    if es_generala(tirada):
        print('Generala!')
        return True
    #print('Elijo el: ', numero_buscado,'Tirar ',dados_por_tirar, ' dado/s')
    resultado = [numero_buscado]*(5-dados_por_tirar)

    #print('Tirada ', 2)
    tirada = tirar(dados_por_tirar)
    #print(tirada)
    if numero_buscado in tirada:
        apariciones = Counter(tirada).get(numero_buscado)
        dados_por_tirar -= apariciones
        resultado_tirada = [numero_buscado]*apariciones
        resultado += resultado_tirada
        #print(f'Salio el {numero_buscado}, {apariciones} vez/veces')
        #print(resultado)
        if es_generala(resultado):
            print('Generala!')
            return True

    #print('Tirada ', 3)
    tirada = tirar(dados_por_tirar)
    #print(tirada)
    if numero_buscado in tirada and len(set(tirada)) == 1:
        #print(resultado)
        print('Generala!')
        return True
    else:
        resultado_tirada = tirada
        resultado += resultado_tirada
        #print('Final: ', resultado)
        return False

# %% Prueba


N = 100000

G = sum([jugar_generala() for i in range(N)])
prob = G/N
print(f'Jugué {N} veces, de las cuales {G} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')
