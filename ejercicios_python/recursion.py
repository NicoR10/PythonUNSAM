
def numero_triangular(n):
    if n == 1:
        return 1
    return n + numero_triangular(n-1)

if __name__ == '__main__':
    res = numero_triangular(2)
    print(res)
