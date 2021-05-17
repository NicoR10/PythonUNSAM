from fileparse import parse_csv

def leer_camion(nombre_de_archivo):
    '''
    Lee los datos de un archivo "camion.csv" utilizando parse_csv
    Retorna un diccionario del tipo {campo1: registro1,..., campoN: registroN}
    '''
    camion = parse_csv('Data/camion.csv', select=['nombre','cajones','precio'], types=[str,int,float])
    return camion

def leer_precios(nombre_de_archivo):
    '''
    Lee los datos del archivo "precios.csv" utilizando parse_csv sin encabezados
    Retorna un diccionario del tipo {campo1: registro1,..., campoN: registroN}
    '''
    precios = {}
    lista_precios = parse_csv('Data/precios.csv',types=[str,float], has_headers=False)
    for tupla in lista_precios:
        precios[tupla[0]] = float(tupla[1])
    return precios

def hacer_informe(camion, precios):
    '''
    Realiza los cálculos necesarios para entregar un informe de los datos
    del camión.
    Devuelve una lista de tuplas.
    '''
    informe = []
    for cajones in camion:
        nombre = cajones['nombre']
        cantidad_cajones = cajones['cajones']
        precio = precios[nombre]
        precio_de_costo = cajones['precio']
        cambio = precio - precio_de_costo
        informe.append((nombre, cantidad_cajones, precio_de_costo, cambio))
    return informe

def imprimir_informe(informe):
    '''
    Imprime el informe en pantalla
    '''
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    tira = '-'*10
    for header in headers:
        print(f'{header:>10s}', end=' ')
    print('')
    for header in headers:
        print(tira, end='  ')
    print('')
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} ${precio:>10.2f} {cambio:>10.2f}')

camion = leer_camion('Data/camion.csv')
precios = leer_precios('Data/precios.csv')
informe = hacer_informe(camion, precios)
imprimir_informe(informe)
