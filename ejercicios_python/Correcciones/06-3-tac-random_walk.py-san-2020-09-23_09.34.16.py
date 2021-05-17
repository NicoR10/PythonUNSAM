# -*- coding: utf-8 -*-
"""
@author: Leandro Santa Cruz
"""

import numpy as np
import matplotlib.pyplot as plt

# X = np.linspace(-np.pi, np.pi, 256)
# C, S = np.cos(X), np.sin(X)

# # plt.plot(X, C)
# # plt.plot(X, S)
# # plt.show()

# plt.figure(figsize = (8, 6), dpi = 80)
# plt.subplot(1,1,1)
# plt.plot(X, C, color = 'blue', linewidth = 1, linestyle = '-')
# plt.plot(X, S, color = 'green', linewidth = 1, linestyle = '-')
# plt.xlim(-4.0, 4.0)
# plt.ylim(-1.0, 1.0)
# plt.yticks(np.linspace(-1, 1, 5))
# plt.show()

def randomwalk(largo):
    pasos = np.random.randint(-1,2,largo)
    return pasos.cumsum()

csl = []
N = 100000
plt.subplot(2,1,1)
for n in range(12):
    cs = randomwalk(N)
    csl.append(cs)
    plt.plot(cs)
    if n == 0:
        maximo = abs(cs[-1])
        nmax = n
        minimo = abs(cs[-1])
        nmin = n
    if abs(cs[-1]) > maximo:
        maximo = abs(cs[-1])
        nmax = n
    if abs(cs[-1]) < minimo:
        minimo = abs(cs[-1])
        nmin = n

# plt.xlabel('Tiempo')
# plt.ylabel('Distancia al origen')
plt.xticks([])
plt.title('12 caminatas al azar')
plt.subplot(2,2,3)
plt.xticks([])
plt.title('La caminata que mas se aleja')
plt.plot(csl[nmax])
plt.subplot(2,2,4)
plt.xticks([]), plt.yticks([])
plt.title('La caminata que menos se aleja')
plt.plot(csl[nmin])