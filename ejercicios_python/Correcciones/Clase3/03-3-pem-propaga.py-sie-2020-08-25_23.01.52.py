# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 17:09:18 2020

@author: Matias
"""

def propagar (lista):
    contador = 0
    while contador <= (len(lista)-1):
        for cont, fosforo in enumerate(lista, start=0):
            if cont == 0 and fosforo == 1:
                lista[cont+1] = 1
            elif cont == 0 and fosforo == -1 or fosforo == 0:
                lista[cont] = fosforo
            elif cont == len(lista)-1 and fosforo == 1:
                lista[cont-1] = 1
            elif cont == len(lista)-1 and fosforo == -1 or fosforo == 0:
                lista[cont] = fosforo
            elif fosforo == 1 and lista[cont-1] == 0 and lista[cont+1] == 0 and cont < len(lista)-1:
                lista[cont-1] = 1
                lista[cont+1] = 1
            elif fosforo == 1 and lista[cont-1] == -1 and lista[cont+1] == 0 and cont < len(lista)-1:
                lista[cont+1] = 1
            elif fosforo == 1 and lista[cont-1] == 0 and lista[cont+1] == -1 and cont < len(lista)-1:
                lista[cont-1] = 1
            elif fosforo == 1 and lista[cont-1] == 1 and lista[cont+1] == 0 and cont < len(lista)-1:
                lista[cont+1] = 1
            elif fosforo == 1 and lista[cont+1] == 1 and lista[cont-1] == 0 and cont < len(lista)-1:
                lista[cont-1] = 1
        contador += 1
    return lista


t1 = [1,0,0,0]
t2 = [0,-1,0,0,1]
t3 = [0,-1,0,-1,1]
t4 = [0 for x in range(10)]
t5 = [1 for x in range(100)]
t6 = [(x%3)-1 for x in range(30)]

tests = [t1, t2, t3, t4 , t5, t6]

for t in tests:
    print('In: ', t)
    print('Out: ', propagar(t))
    print('----------')