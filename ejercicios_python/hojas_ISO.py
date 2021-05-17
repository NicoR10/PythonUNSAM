def A(n):
    # Condición de corte o caso base
    if n == 0:
        return [841, 1189]
    # Reducción del problema (para asegurar que converge al caso base) (n-1)
    res = A(n-1)
    return [min(res), max(res)//2]

if __name__ == '__main__':
    res = A(4)
    print(res)
