print('       ', end=' ')

for i in range(10):
    print(f'{i:<3d}', end=' ')

separador= '-' 
print('') 
print('------', end='')  
for _ in range(10):
    print(f'{separador:-<4}', end='')
  
print('')    
for i in range(10):
    print(f'{i:<6d}:', f'{0:<3d}', f'{i:<3d}', f'{2*i:<3d}', f'{3*i:<3d}', f'{4*i:<3d}', f'{5*i:<3d}', f'{6*i:<3d}', f'{7*i:<3d}', f'{8*i:<3d}', f'{9*i:<3d}')