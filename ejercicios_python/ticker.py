from vigilante import vigilar
import csv
import informe

# formato_tabla.py ----------------------------------------------------------

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
        
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print('<tr><th>', end='')
        print('</th><th>'.join(headers), end='')
        print('</th></tr>')

    def fila(self, data_fila):
        print('<tr><td>', end='')
        print('</td><td>'.join(data_fila), end='')
        print('</td></tr>')
   
def crear_formateador(fmt):
    if fmt == 'txt':
        formateador = FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = FormatoTablaCSV()
    elif fmt == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    return formateador

# ----------------------------------------------------------------------------

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, float])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila
            
def ticker(archivo_referencia, archivo_vigilar, formato_out):
    camion = informe.leer_camion(archivo_referencia)
    filas = parsear_datos(vigilar(archivo_vigilar))
    filas = filtrar_datos(filas, camion)
    if formato_out.lower() == 'csv':
        formateador = crear_formateador(formato_out.lower())
        formateador.encabezado(['Nombre','Precio','Volumen'])
        for fila in filas:
            linea = [str(v) for v in fila.values()]
            formateador.fila(linea)
    elif formato_out.lower() == 'txt':
        formateador = crear_formateador(formato_out.lower())
        formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
        for fila in filas:
            for nombre, precio, volumen in [fila.values()]:
                rowdata = [ nombre, f'{precio:0.2f}', f'{volumen:0.2f}' ]
                formateador.fila(rowdata)

if __name__ == '__main__':
    ticker('Data/camion.csv', 'Data/mercadolog.csv', 'csv')