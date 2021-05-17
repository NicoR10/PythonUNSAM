frase = 'Todos, tu también todos somos programadores'
palabras = frase.split()
frase_t = ''
for palabra in palabras:
    tieneComa = False
    if ',' in palabra:
        palabra = palabra.replace(',','',1)
        tieneComa = True
    if 'o' in palabra[-2:-1]:
        palabraInclusiva = palabra[::-1].replace('o', 'e', 1)[::-1]
        if tieneComa:
            frase_t += palabraInclusiva + ',' + ' '
        else:
            frase_t += palabraInclusiva + ' '
    else:
        if tieneComa:
            frase_t += palabra + ',' + ' '
        else:
            frase_t += palabra + ' '
print(frase_t)

# Output:
#'Todes, tu también'