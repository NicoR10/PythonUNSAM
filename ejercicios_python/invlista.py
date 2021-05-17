# Según propuesta
def invertir_lista(lista):
    n = len(lista)
    invertida = [1 for _ in lista]
    for e in lista:  # Recorro la lista
        # agrego el elemento e al final de la lista invertida
        n -= 1
        invertida[n] = e
    return invertida


# Pythonica
def invertir(lista):
    return lista[::-1]


print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))

print(invertir([1, 2, 3, 4, 5]))
print(invertir(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
