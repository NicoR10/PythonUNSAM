import random
import numpy as np

mediciones = list()
N = 999
temperatura_real = 37.5

for i in range(N):
    error_gaussiano = random.normalvariate(0, 0.2)
    medicion = temperatura_real + error_gaussiano
    mediciones.append(round(medicion, 2))
    print(round(medicion, 2))

maximo = max(mediciones)
minimo = min(mediciones)
promedio = sum(mediciones)/len(mediciones)

mediciones_ordenadas = mediciones.copy()
mediciones_ordenadas.sort()
mediana = mediciones_ordenadas[len(mediciones_ordenadas)//2]

# %% Guardar array a archivo

temperaturas = np.array(mediciones)
np.save('Data/Temperaturas', temperaturas,)


# %% Resultados

print(f'''El valor máximo es: {maximo}
El valor mínimo es: {minimo}
El valor promedio es: {promedio}
La mediana es: {mediana}''')
