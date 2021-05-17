# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 09:53:47 2020

@author: marco
"""


import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum() # cumulative sum 
    


N = 100000
lista = []

for i in range(12):
    lista.append(randomwalk(N))

dist_max = 0
dist_min = 1000
     
for e in lista:
    if dist_max < abs(e[N-1]):
        dist_max = abs(e[N-1])
        mayor = e    
    if dist_min > abs(e[N-1]):
        dist_min = abs(e[N-1])
        menor = e


fig = plt.figure()
plt.subplot(2,1,1)
plt.title('Total 12 caminatas')
for l in lista:
    plt.plot(l)
    plt.xticks([])


plt.subplot(2, 2, 3)
plt.plot(mayor,color='red')
plt.title('La que mas se aleja',fontsize = 8)
plt.xticks([])
plt.yticks([-500, 0, 500])
          
plt.subplot(2, 2, 4)
plt.plot(menor, color='blue')
plt.title('La que menos se aleja', fontsize = 8)
plt.xticks([])
plt.yticks([0])
        
plt.show()
