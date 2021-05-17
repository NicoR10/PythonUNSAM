#!/usr/bin/env python3
import fileparse
import formato_tabla
from camion import Camion
from lote import Lote


def leer_camion(filename):
    '''
    Lee un archivo con el contenido de un camión 
    y lo devuelve como un objeto Camion.
    '''
    with open(filename) as file:
        camiondicts = fileparse.parse_csv(file,
                                        select=['nombre','cajones','precio'],
                                        types=[str,int,float])

    camion = [ Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts ]
    return Camion(camion)


def leer_precios(nombre_de_archivo):
    '''
    Lee los datos del archivo "precios.csv" utilizando parse_csv sin encabezados
    Retorna un diccionario del tipo {campo1: registro1,..., campoN: registroN}
    '''
    precios = {}
    with open('Data/precios.csv') as file:
        lista_precios = fileparse.parse_csv(file ,types=[str,float], has_headers=False)
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
        nombre = cajones.nombre
        cantidad_cajones = cajones.cajones
        precio = precios[nombre]
        precio_de_costo = cajones.precio
        cambio = precio - precio_de_costo
        informe.append((nombre, cantidad_cajones, precio_de_costo, cambio))
    return informe


def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        #precio = '$ ' + str(round(precio,2))
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)
        
def informe_camion(archivo_camion, archivo_precios, fmt='txt'):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)


def main(parametros):
    # Analiza la línea de comandos
    if len(parametros) == 3:
        informe_camion(parametros[1], parametros[2])
    elif len(parametros) == 4:
        formato = parametros[3].lower()
        informe_camion(parametros[1], parametros[2], fmt=formato)
    else:
        print('Necesita dos rutas a archivos')


if __name__ == '__main__':
    import sys
    main(sys.argv)
