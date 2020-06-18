import random

class Borracho:
    """Clase borracho. Creamos instancia de quien se movera.
    Parametro: Nombre
    """
    def __init__(self, nombre):
        self.nombre = nombre
    

class BorrachoTradicional(Borracho):
    """Clase BorrachoTradicional hereda de Borracho.
    Contiene método camina()
    """
    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self): 
        """Método caminar que devolverá la dirección a la que ira.
        Con random.choice elegimos un elemento aleatoriamente de la lista.
        """
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

class BorrachoBailarin(Borracho):
    """Clase BorrachoBailarin hereda de Borracho.
    """
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def camina(self):
        return random.choice([(5, 1), (2, -1), (-1, 6), (-3, -1)])