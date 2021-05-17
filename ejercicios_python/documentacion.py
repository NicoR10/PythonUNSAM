def valor_absoluto(numero_real):
    '''
    Calcula el valor absoluto de un número real.
    PRE: Recibe como parámetro un numero real (int, float)
    POST: Devuelve el valor absoluto del número real.
    '''
    if numero_real >= 0:
        return numero_real
    else:
        return -numero_real


def suma_pares(lista):
    '''
    Suma los elementos pares de una lista de numeros enteros.
    PRE: Recibe una lista de numeros enteros.
    POST: Devuelve la suma de los numeros pares de la lista.
    '''
    resultado = 0  # Invariante de ciclo
    for numero in lista:
        if numero % 2 == 0:
            resultado += numero
        else:
            resultado += 0
    return resultado


def veces(a, b):
    ''' 
    Realiza la suma sucesiva de a. b veces
    PRE: El objeto a sabe resolver la operacion +
    POST: Devuelve el resultado de aplicar la suma sucesiva sobre a, b cantidad de veces
    '''
    res = 0 #  Invariante de ciclo
    nb = b #  Invariante de ciclo
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res


def collatz(n):
    '''
    Calcula la cantidad de pasos en la conjetura de collatz para llegar a 1
    partiendo de un numero positivo entero n.
    PRE: n es un numero positivo entero
    POST: devuelve la cantidad de pasos necesarios de la conjetura hasta llegar al 1
    '''
    res = 1 #  invariante de ciclo

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res