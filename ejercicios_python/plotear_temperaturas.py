import matplotlib.pyplot as plt
import numpy as np

temperaturas = np.load('Data/Temperaturas.npy')

plt.figure('Temperaturas')
plt.hist(temperaturas, bins=100, color='red')
