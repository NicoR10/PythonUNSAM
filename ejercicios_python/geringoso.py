
vocales = ['a', 'e', 'i', 'o', 'u'] 
cadena = "Geringoso"
cadenaGeringosa = ''
for c in cadena:
    if c in vocales:
        cadenaGeringosa += (c + 'p' + c)
    else:
        cadenaGeringosa += c
    
print(cadenaGeringosa)

