
def pascal(n, k):
    if k == 0 or n==k:
        return 1
    return pascal(n-1, k-1) + pascal(n-1, k)    

if __name__ == '__main__':
    
    resultado = pascal(5,2)
    print(resultado)