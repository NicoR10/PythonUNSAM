import random
import matplotlib.pyplot as plt

lista_1 = [1, 2, -3, 8, 1, 5]
lista_2 = [1, 2, 3, 4, 5]
lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
lista_4 = [10, 8, 6, 2, -2, -5]
lista_5 = [2, 5, 1, 0]

def ord_burbujeo(lista):
    comp_nico = 0
    array = lista.copy()
    for i in range(len(array), 0, -1):
        for j in range(i-1):
            comp_nico += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array, comp_nico

ordenada_1, comp_nico1 = ord_burbujeo(lista_1)
ordenada_2, comp_nico2 = ord_burbujeo(lista_2)
ordenada_3, comp_nico3 = ord_burbujeo(lista_3)
ordenada_4, comp_nico4 = ord_burbujeo(lista_4)
ordenada_5, comp_nico5 = ord_burbujeo(lista_5)

comp = []
largo = list(range(1, 257))
n_cuadrado = [n**2 for n in largo]
o_n = [n for n in largo]
for n in range(1, 257):
    lista = [random.randint(0,1000) for _ in range(n)]
    ordenada, comparaciones = ord_burbujeo(lista)
    comp.append(comparaciones)  
    
plt.figure(1)
plt.plot(comp, label='Burbujeo')
plt.plot(n_cuadrado, label='O(n2)')
plt.plot(o_n, label='O(n)')
plt.xlim([1, 100])
plt.ylim([0, 300])
plt.legend(title='Comparaciones')