
class Coordenada:
    """Clase Coordenada guardara las coordenadas de nuestro agente
    - constructor:
        Define posiciones iniciales.
    - mover(): Variaciones de las coordenadas
    - distancia()
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mover(self, delta_x, delta_y):
        """Método mover recibe variaciones de movimientos. Cuanto se moverá
        Y cuando se mueve a las coordenadas actuales se les
        suma las coordenadas X e Y que ingresan como parámetros.
        """
        return Coordenada(self.x + delta_x, self.y + delta_y)
     
    def distancia(self, otra_coordenada):
        """Método distancia del agente con respecto a unas coordenadas. 
        Devuelve la distancia calculando con el Teorema de Pitágoras.
        """
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y

        return (delta_x**2 + delta_y**2)**0.5