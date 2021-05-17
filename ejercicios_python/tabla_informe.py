import csv

def leer_camion(nombre_de_archivo):
    camion = []
    with open(nombre_de_archivo) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for line in reader:
            valores = [line[0], int(line[1]), float(line[2])]
            lote = dict(zip(headers, valores))
            camion.append(lote)
    return camion

def leer_precios(nombre_de_archivo):
    precios = {}
    with open(nombre_de_archivo) as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            try:
                precios[line[0]] = float(line[1])
            except IndexError:
                #print('Línea vacía: ', e)
                pass
    return precios

def hacer_informe(camion, precios):
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

