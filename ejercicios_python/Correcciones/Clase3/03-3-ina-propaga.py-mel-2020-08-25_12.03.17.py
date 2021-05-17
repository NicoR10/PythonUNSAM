#%%
#Ejercicio 3.9. Propagación.
def propagar(vector):
    vector_propagado = vector.copy()
    for i, e in enumerate(vector):
        if e == 1:
            for z in range(i,0,-1):
                if vector[z-1] == 0:
                    vector_propagado[z-1]=1
                else:
                    break
            for x in range(i,len(vector),1):
                if vector[x]==-1:
                    break
                else:
                    vector_propagado[x]=1
    return vector_propagado
print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 1]))
print(propagar([ 0, 0, 0, 1, 0, 0]))

t1 = [1,0,0,0]
t2 = [0,-1,0,0,1]
t3 = [0,-1,0,-1,1]
t4 = [0 for x in range(10)]
t5 = [1 for x in range(100)]
t6 = [(x%3)-1 for x in range(30)]

tests = [t1, t2, t3, t4 , t5, t6]

for t in tests:
    print(t)
    print(propagar(t))


