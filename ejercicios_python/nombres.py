from itertools import permutations 
  
# Get all permutations of [0, 1, 2, 3]
perm = permutations([0, 1, 2, 3])

#iniciales = ['N', 'F', 'S', 'A']
#iniciales = ['LA', 'RA', 'MA', 'VA']
#iniciales = ['PI', 'RA', 'MA', 'VA']
# iniciales = ['L', 'R', 'M', 'A']
#iniciales = ['LA', 'R', 'MA', 'G']
#iniciales = ['IR','A','S','N']
#iniciales = ['ACOUS', 'I', 'R','']
iniciales = ['R', 'A', 'I', 'Acoust']
numero = 1
opcion = 1
# Print the obtained permutations
for combinacion in list(perm):
    print(f'Opción {opcion}: ',iniciales[combinacion[0]] + iniciales[combinacion[1]] + iniciales[combinacion[2]] + iniciales[combinacion[3]])
    opcion += 1
                