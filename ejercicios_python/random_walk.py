import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint(-1,2,largo)    
    return pasos.cumsum()

def generar_caminatas(cantidad, N):
    caminatas = list()
    for i in range(cantidad):
        caminata = randomwalk(N)
        caminatas.append(caminata)
    return caminatas

def main():
    
    N = 100000
    CANTIDAD = 12
    
    caminatas = generar_caminatas(CANTIDAD, N)
    maximo_por_caminata = [max(abs(caminata)) for caminata in caminatas]
    caminata_alejada = caminatas[maximo_por_caminata.index(max(maximo_por_caminata))]
    caminata_cercana = caminatas[maximo_por_caminata.index(min(maximo_por_caminata))]
    
    fig = plt.figure(1, figsize=(10, 6))
    
    plt.subplot(2, 1, 1) # define la figura de arriba
    for caminata in caminatas:
        plt.plot(caminata)
    plt.title('12 caminatas al azar')
    plt.yticks([-500, 0, +500])
    plt.ylim(-800, 800)
    plt.xticks([])
    
    plt.subplot(2, 2, 3)
    plt.plot(caminata_alejada)
    plt.title('La caminata que mas se aleja')
    plt.yticks([-500, 0, +500])
    plt.ylim(-800, 800)
    plt.xticks([])
    
    plt.subplot(2, 2, 4)
    plt.plot(caminata_cercana)
    plt.title('La caminata que menos se aleja')
    plt.yticks([-500, 0, +500])
    plt.ylim(-800, 800)
    plt.xticks([])
    
    plt.show()
    
if __name__ == '__main__':
    main()