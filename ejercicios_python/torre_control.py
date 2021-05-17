class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

class TorreDeControl:
    
    def __init__(self):
        self.cola_de_arribo = Cola()
        self.cola_de_partida = Cola()
        
    def nuevo_arribo(self, codigo):
        self.cola_de_arribo.encolar(codigo)
        
    def nueva_partida(self, codigo):
        self.cola_de_partida.encolar(codigo)
        
    def ver_estado(self):
        print('Vuelos esperando para aterrizar:', end=' ')
        print(', '.join(self.cola_de_arribo.items))
        print('Vuelos esperando para despegar:', end=' ')
        print(', '.join(self.cola_de_partida.items))
        
    def asignar_pista(self):
        hay_arribos = not self.cola_de_arribo.esta_vacia()
        hay_partidas = not self.cola_de_partida.esta_vacia()
        
        if hay_arribos:
            vuelo_asignado = self.cola_de_arribo.desencolar()
            print(f'El vuelo {vuelo_asignado} aterrizó con éxito')
        elif hay_partidas:
            vuelo_asignado = self.cola_de_partida.desencolar()
            print(f'El vuelo {vuelo_asignado} despegó con éxito')
        else:
            print('No hay vuelos en espera.')
        