# Mi versión

class Canguro:
    
    def __init__(self):
        self.contenido_marsupio = []
        
    def meter_en_marsupio(self, elemento):
        self.contenido_marsupio.append(elemento)
        
    def __str__(self):
        return f'Canguro que contiene: {self.contenido_marsupio}'

# Versión corregida de canguro_malo

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido.copy() # Acá estaba. Agregué el copy()

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)
        
'''
Sin el copy() todos los objetos de la clase que vengan sin contenido por
defecto, referenciaban a la misma lista vacía.
''' 