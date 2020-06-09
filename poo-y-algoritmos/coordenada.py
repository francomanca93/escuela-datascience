
class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return(x_diff + y_diff)**0.5


if __name__ == "__main__":
    coordenada_1 = Coordenada(3, 30)
    coordenada_2 = Coordenada(4, 8)

    print(coordenada_1.distance(coordenada_2))
    print(isinstance(coordenada_1, Coordenada))