import csv
import sys

def costo_camion(nombre_de_archivo):
    with open(nombre_de_archivo) as csv_file:
        reader = csv.reader(csv_file)
        cabeceras = next(reader)
        costo = 0
        for linea in reader:
            costo += float(linea[1]) * float(linea[2])
    return costo
    
if(len(sys.argv) == 2):
    nombre_de_archivo = sys.argv[1]    
else:
    nombre_de_archivo = 'Data/camion.csv'

costo = costo_camion(nombre_de_archivo)
print('Costo total: ', round(costo,2))