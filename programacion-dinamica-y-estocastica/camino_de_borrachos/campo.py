
class Campo: 
    """Creamos un campo donde ubicaremos al borracho.
    En el campo podremos:
        - añadir_borracho()
        - mover_borracho()
        - obtener_coordenada() del borracho
    """

    def __init__(self):
        """Nuestra clase tendrá como atributo un diccionario.
        """
        self.coordenada_de_borrachos = {}
    
    def añadir_borracho(self, borracho, coordenada):
        """Añadimos un agente a nuestro diccionario.
        Nuestra llave sera nuestro parámetro "borracho" y tendrá el valor asignado "coordenada"
        que es una clase Coordenada creado en coordenada.py.
        """
        self.coordenada_de_borrachos[borracho] = coordenada
    
    
    def mover_borracho(self, borracho):
        """Recibe un borracho y lo movemos.
        Parametro: 
        - delta_x, delta_y:
            Al mover a nuestro agente ejecutamos el método camina de la clase BorrachoTradicional
            devolviendo la dirección hacia donde se movió.
        - coordenada_actual:
            Obtenemos las coordenadas del borracho
        - nueva_coordenada:
            Del objeto Coordenada ejecutamos el método mover con los parámetros
            que el objeto borracho genero. El resultado lo guardamos en nueva_coordenada.
        - self.coordenada_de_borrachos[borracho]:
            El objeto guardado en nueva_coordenada ahora estará asociado a la llave de borracho.
        """
        
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenada_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)
        self.coordenada_de_borrachos[borracho] = nueva_coordenada
    
    def obtener_coordenada(self, borracho):
        """Metodo que nos devuelve las coordenadas del borracho
        """
        return self.coordenada_de_borrachos[borracho]