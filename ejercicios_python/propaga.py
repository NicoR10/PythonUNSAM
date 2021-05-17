def propagar(lista):
    final_index = len(lista) - 1
    for i, fosforo in enumerate(lista):
        if fosforo == 1:
            j = i
            k = i
            while j >= 0:
                j -= 1
                if lista[j] == 0:
                    lista[j] = 1
                else:
                    break
            while k < final_index:
                k += 1
                if lista[k] == 0:
                    lista[k] = 1
                else:
                    break
    return lista


lista1 = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
print(lista1)
print(propagar(lista1))

lista2 = [0, 0, 0, 1, 0, 0]
print(lista2)
print(propagar(lista2))
