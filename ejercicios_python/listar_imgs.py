#!/usr/bin/env python3

# Import (bibliotecas)
import os

# Funcion principal
def main(ruta):
    cantidad_de_archivos = 0
    for root, dirs, files in os.walk(ruta):
        for nombre in files:
            extension = nombre[-4:]
            if '.png' in extension or '.PNG' in extension:
                print(nombre)
                cantidad_de_archivos += 1
    print(f'Se encontraron {cantidad_de_archivos} archivos con extensión ".png"')


if __name__ == '__main__':
    import sys
    parametros = sys.argv
    if len(parametros) == 2:
        main(parametros[1])
    else:
        print('Debe especificar una ruta. Intente nuevamente...')
