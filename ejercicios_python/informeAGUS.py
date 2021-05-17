import csv


def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers,row))
            camion.append(record)
                     
    return camion


def leer_precios(nombre_archivo):
    precios = {}
    
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
                
        try:
            for row in rows:
                precios.update({row[0] : row[1]})
        
        except IndexError:
            print('Puede haber problemas por el índice ingresado en la función "leer_precios".\n')            
            
    return precios
    
#%% Ejecución de funciones para informe
camion = leer_camion(r'Data\fecha_camion.csv')
precios = leer_precios('Data\precios.csv')

#%% Calculos necesarios para realizar el informe
costo_camion = 0 
for fila in camion:
    costo_camion += int(fila.get('cajones')) * float(fila.get('precio'))
    
recaudado = 0
for fila in camion:
    recaudado += int(fila.get('cajones')) * float(precios.get(fila['nombre']))

diferencia, balance = round(recaudado - costo_camion,2), '' 
if diferencia > 0:
    balance = 'ganancia'
else:
    balance = 'perdida'

print(f'''Informe:\nEl costo del camion fue de ${costo_camion}
Lo recaudado por la venta del camion fue de ${recaudado}
La {balance} fue de ${diferencia}''')