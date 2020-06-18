
from borracho import BorrachoTradicional, BorrachoBailarin
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show


def caminata(campo, borracho, pasos):
    """función caminata. Será eñ campo donde se moverá el borracho realizando sus pasos  
    Recibe: campo, borracho y pasos

    - inicio: Obtenemos las coordenadas actuales de la llave "borracho".
    - bucle: En el bucle Repetiremos la misma cantidad de pasos definidos moviendo al borracho
    
    @return: Devolveremos la distancia entre las coordenadas de la instancia inicio y campo.
    """
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
    
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    """Simulación de una caminata
    Recibimos: pasos, numeros de intentos, tipo de borracho

    Parametros: 
    - borracho. Objeto que define al borracho
    - origen. Objeto que inicializa el origen
    - distancias[]. Lista
    
    - bucle: Para cada intento, 
        - Creamos una instancia de Campo.
        - Añadimos un borracho al campo.
        - Obtenemos la distancia final de la simulación.
        - El resultado lo guardamos en la lista de distancias.

    @return: Retornamos la lista de distancias.
    """
    borracho = tipo_de_borracho(nombre='Franco')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.añadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias

def graficar(x, y):
    """Método para graficar.
    Recibimos valores para ejes.
    - Creamos una instancia de figure, con su titulo y las etiquetas de los ejes.
    - Ingresamos los datos de X e Y.
    - Generamos una gráfica en HTML.
    """
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend='distancia media')

    show(grafica)

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    """Función principal que crea la simulación.

    Parametro: Lista que guardara el promedio de cada caminata.
    
    - Bucle. Por cada ítem en nuestras series de caminata:
        - Guardamos las distancias que generan todas las simulaciones definido en numero_de_intentos.
        - De la lista de distancias obtenemos la distancia promedio.
        - De la lista de distancias obtenemos el máximo valor.
        - De la lista de distancias obtenemos el menor valor.
        - Guardamos el promedio de la caminata en la lista distancias_media_por_caminata.
        - Imprimimos los datos de la caminata actual.
        
    Graficamos la información de las distancias finales según la cantidad de pasos.
    """
    distancias_media_por_caminata = []

    for paso in distancias_de_caminata:
        distancias = simular_caminata(paso, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatorio de {paso} pasos')
        print(f'Media = {distancia_media}')
        print(f'Maxima = {distancia_maxima}')
        print(f'Minima = {distancia_minima}')
    graficar(distancias_de_caminata, distancias_media_por_caminata)


if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)