from informe import leer_camion


def costo_camion(nombre_de_archivo):
    '''
    Lee el archivo "camion.csv" y devuelve el costo total del camión.
    '''
    camion = leer_camion(nombre_de_archivo)
    return sum([dic['cajones']*dic['precio'] for dic in camion])


costo = costo_camion('Data/camion.csv')
print('Costo total: ', round(costo, 2))
