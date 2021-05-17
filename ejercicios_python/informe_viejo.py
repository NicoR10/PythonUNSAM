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
            except IndexError as e:
                print('Línea vacía: ', e)
    return precios


camion = leer_camion('Data/camion.csv')
precios = leer_precios('Data/precios.csv')

ventas = 0
costos = 0

for cajones in camion:
    nombreDeFruta = cajones['nombre']
    cantidad = cajones['cajones']
    precio_de_venta = precios[nombreDeFruta]
    precio_de_costo = cajones['precio']
    ventas += cantidad*precio_de_venta
    costos += cantidad*precio_de_costo

balance = ventas - costos

print(f'''Informe: Balance (Ventas - Costos) -> ${round(balance,2)}''')
