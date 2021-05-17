import random
import matplotlib.pyplot as plt
import time
import timeit as tt

def ord_burbujeo(lista):
    comparaciones = 0
    array = lista.copy()
    for i in range(len(array), 0, -1):
        for j in range(i-1):
            comparaciones += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return comparaciones

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    comparaciones = 0   
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        comparaciones += 1
        if lista[i + 1] < lista[i]:
            comparaciones += reubicar(lista, i + 1)
        #print("DEBUG: ", lista)
    return comparaciones

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]
    comparaciones = 0
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        comparaciones += 2
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    return comparaciones
    
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    comparaciones = 0
    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p, comp = buscar_max(lista, 0, n)
        comparaciones += comp
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1
    return comparaciones

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    comparaciones = 0
    pos_max = a
    for i in range(a + 1, b + 1):
        comparaciones += 1
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max, comparaciones

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    comparaciones = 0
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq, comp_1 = merge_sort(lista[:medio])
        der, comp_2 = merge_sort(lista[medio:])
        lista_nueva, comp_3 = merge(izq, der)
        comparaciones = comp_1 + comp_2 + comp_3
    return lista_nueva, comparaciones

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    comparaciones = 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        comparaciones += 3
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comparaciones

def generar_lista(n):
    return [random.randint(0,1000) for _ in range(n)]

tiempo_seleccion = []
tiempo_insercion = []
tiempo_burbujeo = []
tiempo_mergesort = []

for n in range(1, 257):
    lista = generar_lista(n)
    
    t_sel = tt.timeit('ord_seleccion(lista.copy())', number=10, globals= globals())
    tiempo_seleccion.append(t_sel)
    

    t_ins = tt.timeit('ord_insercion(lista.copy())', number=10, globals= globals())
    tiempo_insercion.append(t_ins)
    
    t_bur = tt.timeit('ord_burbujeo(lista.copy())', number=10, globals= globals())
    tiempo_burbujeo.append(t_bur)
    
    t_mer = tt.timeit('merge_sort(lista.copy())', number=10, globals= globals())
    tiempo_mergesort.append(t_mer)
        
plt.figure(1)
plt.plot(tiempo_seleccion, 'b--', linewidth=3, label='Selección')
plt.plot(tiempo_insercion, 'r', linewidth=1, label='Inserción')
plt.plot(tiempo_burbujeo, 'g--', linewidth=2.5, label='Burbujeo')
plt.plot(tiempo_mergesort, 'k--', linewidth=2, label='Merge Sort')
plt.xlim([100, 256])
plt.legend()
