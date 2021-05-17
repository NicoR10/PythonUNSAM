def donde_insertar(lista, x):
    '''
    Recibe una lista ordenada y un valor.
    Devuelve la posición en la cual se debería insertar el valor, o si el 
    elemento ya existe, la posición en la que se encuentra.
    '''
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio      # elemento encontrado!
            break
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:                # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    pos = medio  # Agregado para que devuelva donde insertar
    return pos


def insertar(lista, x):
    '''
    Recibe una lista ordenada y un valor (x).
    Si el valor se encuentra en la lista, devuelve su posición. De lo contrario,
    lo inserta en la lista de modo que permanezca ordenada y devuelve la posición en
    la cual se insertó el valor.
    '''
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio      # elemento encontrado!
            break
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:                # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    if pos == -1:
        lista.insert(medio, x)
        pos = medio
    return pos

test1 = donde_insertar([0, 2, 4, 6], 3)
test2 = donde_insertar([0, 2, 4, 6], 4)
print(test1)
print(test2)

test3 = insertar([1, 2, 4], 3)
test4 = insertar([1, 2, 4], 2)
print(test3)
print(test4)
