def buscar_u_elemento(lista, elemento):
    '''
    Busca en la lista un elemento, si no lo encuentra devuelve -1
    '''
    if elemento not in lista:
        return -1
    else:
        for i, valor in enumerate(lista):
            if valor == elemento:
                return i


def maximo(lista):
    '''Devuelve el máximo de una lista,
    la lista debe ser no vacía y de números positivos.
    '''
    m = 0
    for e in lista:  # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m


print(buscar_u_elemento([1, 2, 3, 4, 5], 4))
print(buscar_u_elemento([1, 2, 3, 4, 5], 6))

print(maximo([1, 2, 3, 4, 5]))
print(maximo([1, 2, 3, 4, 5, 120]))
