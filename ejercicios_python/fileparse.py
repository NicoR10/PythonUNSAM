import csv

def parse_csv(file, select=None, types=None, has_headers=True, silence_errors = False):
    '''
    Parsea un iterable CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el
    parámetro select, que debe ser una lista de nombres
    de las columnas a considerar.
    '''
    filas = csv.reader(file)
    # Lee los encabezados del archivo
    if has_headers:
        encabezados = next(filas)
    # Si se indicó un selector de columnas,
    #    buscar los índices de las columnas especificadas.
    # Y en ese caso achicar el conjunto de encabezados para diccionarios
    if select:
        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
        encabezados = select
    else:
        indices = []

    registros = []
    for nro_fila, fila in enumerate(filas, 1):
        if not fila:    # Saltear filas vacías
            continue
        # Filtrar la fila si se especificaron columnas
        if indices:
            fila = [fila[index] for index in indices]

        # Armar el diccionario o la tupla.
        if types:
            try:
                fila = [func(val) for func, val in zip(types, fila)]
            except ValueError as e:
                if silence_errors:
                    continue
                else:
                    print(f'Row {nro_fila}: No pude convertir {fila}')
                    print(f'Motivo {nro_fila}: {e}')
        if has_headers:
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
        else:
            fila = tuple(fila)
            registros.append(fila)
    return registros
