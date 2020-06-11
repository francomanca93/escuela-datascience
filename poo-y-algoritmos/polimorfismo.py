
# Clase padre
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print('Ando caminando')

# Clase hija
class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print('Ando moviendome en mi bicicleta')

# Función de entrada
def main():
    persona = Persona('Franco')
    persona.avanza()

    ciclista = Ciclista('Federico')
    ciclista.avanza()


if __name__ == '__main__':
    main()